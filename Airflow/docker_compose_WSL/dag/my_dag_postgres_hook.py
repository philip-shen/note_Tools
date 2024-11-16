import json
from datetime import datetime, timedelta

from airflow.decorators import dag, task
from airflow.hooks.postgres_hook import PostgresHook

default_args = {
    'owner': 'philphoenix',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    dag_id = 'my_dag_postgres_hook_V1',
    description = 'my dag postgres hook',
    default_args = default_args,
    schedule_interval='@daily', 
    start_date=datetime(2024, 11, 15))
def conn_db_run():
    @task()
    def conn_local_db():
        hook = PostgresHook(postgres_conn_id="postgres_docker") 
        # postgres_conn_id => 法一：localhost-db、法二：local-db-cli、法三：local_db
        connection = hook.get_conn()
        cursor = connection.cursor()
        sql_query = """
            SELECT * FROM pg_catalog.pg_tables;
            """
        cursor.execute(sql_query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return(json.dumps(result))

    conn_local_db()

conn_db_run()