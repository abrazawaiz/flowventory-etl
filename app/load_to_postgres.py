import os
import sys
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db_utils import insert_dataframe
from app.settings import DATA_PROCESSED_DIR
from app.logger_utils import get_logger

logger = get_logger("load_to_postgres")

def load_to_postgres():
    try:
        csv_files = [f for f in os.listdir(DATA_PROCESSED_DIR) if f.endswith(".csv")]
        
        if not csv_files:
            raise FileNotFoundError(f"No CSV files found in {DATA_PROCESSED_DIR}")
        
        file_name = csv_files[0]
        file_path = os.path.join(DATA_PROCESSED_DIR, file_name)
        
        logger.info(f"Loading file: {file_name}")
        logger.info(f"File path: {file_path}")

        df = pd.read_csv(file_path)
        row_count = len(df)
        col_count = len(df.columns)
        
        logger.info(f"Dataset shape: {row_count} rows × {col_count} columns")
        logger.info(f"Columns: {', '.join(df.columns)}")

        logger.info("Inserting data into PostgreSQL...")
        insert_dataframe(df, "flowventory_staging.stg_inventory_full")

        logger.info(f"✅ Successfully loaded {row_count} rows into database")
        return True

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise
    except pd.errors.EmptyDataError:
        logger.error("CSV file is empty")
        raise
    except Exception as e:
        logger.error(f"Load to PostgreSQL failed: {e}")
        raise

if __name__ == "__main__":
    load_to_postgres()