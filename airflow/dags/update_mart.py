from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator 
from airflow.operators.python import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime, timedelta
import logging
import requests
from config.clickhouse_config import CLICKHOUSE_HOST, CLICKHOUSE_USER, CLICKHOUSE_PASSWORD

CLICKHOUSE_TABLE = 'orders_mart'
import logging
def execute_clickhouse_query(query):
    url = f"{CLICKHOUSE_HOST}/?query={query}"
    try:
        response = requests.get(url, auth=(CLICKHOUSE_USER, CLICKHOUSE_PASSWORD))
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error executing query: {e}")

def log_error(message, exception=None):
    if exception:
        logging.error(f"{message}: {exception}")
    else:
        logging.error(message)

def log_success(message):
    logging.info(f"Success: {message}")

def log_start():
    logging.info("DAG started: Refreshing data mart.")

def truncate_data_mart():
    query = f"TRUNCATE TABLE {CLICKHOUSE_TABLE}"
    return execute_clickhouse_query(query)

def update_data_mart():
    query = """
    INSERT INTO orders_mart
    SELECT
        o.order_id AS order_id,
        c.name AS client_name,
        c.region AS region,
        p.name AS product_name,
        p.category AS category,
        o.order_date AS order_date,
        o.total_amount AS total_amount,
        d.discount_percent AS discount_percent,
        o.total_amount * (1 - d.discount_percent / 100.0) AS final_amount
    FROM
        orders o
    LEFT JOIN clients c ON o.client_id = c.client_id
    LEFT JOIN products p ON o.product_id = p.product_id
    LEFT JOIN discounts d 
        ON o.product_id = d.product_id
       AND o.order_date BETWEEN d.start_date AND d.end_date
    """
    return execute_clickhouse_query(query)

def log_end():
    logging.info("DAG completed successfully: Data mart refreshed.")


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'refresh_clickhouse_data_mart',
    default_args=default_args,
    description='DAG for refreshing data mart in ClickHouse',
    schedule_interval='@daily', 
)

start_task = PythonOperator(
    task_id='log_start',
    python_callable=log_start,
    dag=dag,
)

truncate_task = PythonOperator(
    task_id='truncate_data_mart',
    python_callable=truncate_data_mart,
    dag=dag,
)

update_task = PythonOperator(
    task_id='update_data_mart',
    python_callable=update_data_mart,
    dag=dag,
)

end_task = PythonOperator(
    task_id='log_end',
    python_callable=log_end,
    dag=dag,
)

start_task >> truncate_task >> update_task >> end_task
