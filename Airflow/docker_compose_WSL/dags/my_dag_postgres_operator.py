from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner': 'philphoenix',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG (
    dag_id = 'my_dag_postgres_operator_V3',
    description= 'my dag postgres operator',
    start_date = datetime(2024, 11, 14),
    schedule_interval = '0 0 * * *'
    ) as dag:
    task1 = PostgresOperator(
        task_id = 'create_postgres_table',
        postgres_conn_id = 'postgres_docker',
        sql = """
            create table if not exists dag_runs (
                date date,
                dag_id character varying,
                primary key (date, dag_id )
            )
        """
    )
    task2 = PostgresOperator(
        task_id = 'insert_postegres_table',
        postgres_conn_id = 'postgres_docker',
        sql = """
            insert into dag_runs (date, dag_id) values ('{{ ds }}', '{{ dag.dag_id }}')
        """
    )
    task3 = PostgresOperator(
        task_id = 'delete_data_from_table',
        postgres_conn_id = 'postgres_docker',
        sql = """
            delete from dag_runs where date = '{{ ds }}' and dag_id = '{{dag.dag_id}}'
        """
    )
    
    task1 >> task3 >> task2