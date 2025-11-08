import os
import sys
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, "/app")
os.chdir("/app")

from extract_data import extract_dataset
from transform_data import transform_data as transform_func
from load_to_postgres import load_to_postgres as load_func

default_args = {
    "owner": "flowventory_team",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="flowventory_etl_dag",
    default_args=default_args,
    description="ETL pipeline for Flowventory",
    schedule_interval="@daily",
    start_date=datetime(2025, 11, 1),
    catchup=False,
    tags=["flowventory", "etl"],
) as dag:
    extract_task = PythonOperator(
        task_id="extract_dataset",
        python_callable=extract_dataset,
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_func,
    )

    load_task = PythonOperator(
        task_id="load_to_postgres",
        python_callable=load_func,
    )

    extract_task >> transform_task >> load_task
