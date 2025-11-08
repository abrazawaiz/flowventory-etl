import os
import sys
import kagglehub
import shutil

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.settings import KAGGLE_DATASET_ID, KAGGLE_CONFIG_DIR, DATA_RAW_DIR
from app.logger_utils import get_logger

logger = get_logger("extract_data")

def extract_dataset():
    try:
        os.environ["KAGGLE_CONFIG_DIR"] = KAGGLE_CONFIG_DIR
        logger.info("Starting dataset extraction from Kaggle...")
        logger.info(f"Kaggle Dataset ID: {KAGGLE_DATASET_ID}")
        logger.info(f"Kaggle Config Dir: {KAGGLE_CONFIG_DIR}")

        dataset_path = kagglehub.dataset_download(KAGGLE_DATASET_ID)
        logger.info(f"Dataset downloaded successfully to: {dataset_path}")

        os.makedirs(DATA_RAW_DIR, exist_ok=True)

        files_copied = 0
        for file in os.listdir(dataset_path):
            src = os.path.join(dataset_path, file)
            dest = os.path.join(DATA_RAW_DIR, file)
            
            if os.path.isfile(src):
                shutil.copy2(src, dest)
                files_copied += 1
                logger.info(f"Copied: {file}")
        
        logger.info(f"✅ {files_copied} file(s) moved to {DATA_RAW_DIR}")
        return True

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise
    except PermissionError as e:
        logger.error(f"Permission denied: {e}")
        raise
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        raise

if __name__ == "__main__":
    extract_dataset()