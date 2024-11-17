from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'philphoenix',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(some_dict, ti):
    print("some dict: ", some_dict)
    first_name= ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Hello World! my name is {first_name} {last_name}, ",
          f"and my age is {age}")

def get_name(ti):
    ti.xcom_push(key="first_name", value='Philip')
    ti.xcom_push(key="last_name", value= 'Shen')

def get_age(ti):
    ti.xcom_push(key='age', value=42)
        
with DAG(
    default_args=default_args, 
    dag_id='my_first_dag_python_operator_V6',
    description='my first dag with python operator',
    start_date=datetime(2024, 11, 15),
    schedule_interval='@daily') as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'some_dict': {'a': 1, 'b': 2}}
    )
    
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )
    
    task3 =PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )
    
    [task2, task3] >> task1