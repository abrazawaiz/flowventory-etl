import pandas as pd
import numpy as np
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.settings import DATA_RAW_DIR, DATA_PROCESSED_DIR
from app.logger_utils import get_logger

logger = get_logger("transform_data")

def fix_number(x):
    if isinstance(x, str) and x.count('.') > 1:
        parts = x.split('.')
        return ''.join(parts[:-1]) + '.' + parts[-1]
    return x

def validate_data(df):
    issues = []
    
    null_skus = df['sku_id'].isnull().sum() if 'sku_id' in df.columns else 0
    if null_skus > 0:
        issues.append(f"Found {null_skus} rows with null SKU IDs")
        
    if 'sku_id' in df.columns:
        duplicates = df.duplicated(subset=['sku_id']).sum()
        if duplicates > 0:
            issues.append(f"Found {duplicates} duplicate SKU IDs")
    
    if 'quantity_on_hand' in df.columns:
        negative_qty = (pd.to_numeric(df['quantity_on_hand'], errors='coerce') < 0).sum()
        if negative_qty > 0:
            issues.append(f"Found {negative_qty} rows with negative quantities")
    
    if issues:
        logger.warning("Data quality issues detected:")
        for issue in issues:
            logger.warning(f"  - {issue}")
    else:
        logger.info("✅ All data quality checks passed")
    
    return df

def transform_data():
    try:
        raw_files = [f for f in os.listdir(DATA_RAW_DIR) if f.endswith(".csv")]
        if not raw_files:
            raise FileNotFoundError(f"No CSV files found in {DATA_RAW_DIR}")
        
        raw_file = raw_files[0]
        raw_path = os.path.join(DATA_RAW_DIR, raw_file)
        
        logger.info(f"Loading raw data: {raw_file}")
        logger.info(f"File path: {raw_path}")
        
        df = pd.read_csv(raw_path)
        initial_rows = len(df)
        logger.info(f"Initial row count: {initial_rows}")

        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
        logger.info(f"Columns: {', '.join(df.columns)}")

        df = df.replace({',': '.', r'\$': '', '%': ''}, regex=True)
        df = df.replace("NaN", np.nan)

        df = df.applymap(fix_number)

        numeric_conversions = 0
        for col in df.columns:
            try:
                original_dtype = df[col].dtype
                df[col] = pd.to_numeric(df[col], errors="ignore")
                if df[col].dtype != original_dtype:
                    numeric_conversions += 1
            except Exception:
                pass
        
        logger.info(f"Converted {numeric_conversions} columns to numeric type")

        if "sku_id" in df.columns:
            before_drop = len(df)
            df = df.dropna(subset=["sku_id"])
            dropped = before_drop - len(df)
            if dropped > 0:
                logger.info(f"Dropped {dropped} rows with null SKU IDs")
        else:
            logger.warning("Column 'sku_id' not found in dataset")

        df = validate_data(df)

        os.makedirs(DATA_PROCESSED_DIR, exist_ok=True)
        
        output_path = os.path.join(DATA_PROCESSED_DIR, "inventory_clean.csv")
        df.to_csv(output_path, index=False)

        logger.info(f"✅ Transformed data saved to {output_path}")
        logger.info(f"Final row count: {len(df)} (from {initial_rows})")
        logger.info(f"Data retention: {len(df)/initial_rows*100:.2f}%")
        
        return True

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise
    except pd.errors.EmptyDataError:
        logger.error("CSV file is empty")
        raise
    except Exception as e:
        logger.error(f"Transformation failed: {e}")
        raise


if __name__ == "__main__":
    transform_data()