from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from stackof_etl import run_stackof_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 2),
    'email': ['ondrejmlynarc@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'stackof_dag',
    default_args=default_args,
    description='stackoverflow etl',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='complete_stackof_etl',
    python_callable=run_stackof_etl,
    dag=dag, 
)

run_etl
