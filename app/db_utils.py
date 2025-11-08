import psycopg2
from psycopg2.extras import execute_values
from app.settings import DB_USER, DB_PASS, DB_NAME, DB_HOST, DB_PORT
from app.logger_utils import get_logger

logger = get_logger("db_utils")

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        logger.info("Database connection established.")
        return conn
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise

def insert_dataframe(df, table_name):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cols = ",".join(list(df.columns))
        values = [tuple(x) for x in df.to_numpy()]
        sql = f"INSERT INTO {table_name} ({cols}) VALUES %s"
        execute_values(cursor, sql, values)
        conn.commit()
        logger.info(f"{len(df)} rows inserted into {table_name}.")
    except Exception as e:
        logger.error(f"Insert failed: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
