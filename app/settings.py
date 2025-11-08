import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

KAGGLE_DATASET_ID = os.getenv("KAGGLE_DATASET_ID")
KAGGLE_CONFIG_DIR = os.getenv("KAGGLE_CONFIG_DIR")

DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_RAW_DIR = os.path.join(DATA_DIR, "raw")
DATA_PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
LOG_DIR = os.path.join(BASE_DIR, "logs")

for path in [DATA_DIR, DATA_RAW_DIR, DATA_PROCESSED_DIR, LOG_DIR]:
    os.makedirs(path, exist_ok=True)
