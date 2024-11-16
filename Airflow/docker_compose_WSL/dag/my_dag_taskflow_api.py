from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args = {
    'owner': 'philphoenix',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    dag_id = 'my_dag_taskflow_api_V1',
    description = '',
    default_args = default_args,
    start_date = datetime(2024, 11, 15),
    schedule_interval = '@daily')
def test_etl():
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Philip',
            'last_name': 'Shen'
        }
    
    @task()
    def get_age():
        return 22
    
    @task()
    def greet(first_name, last_name, age):
        print(f'Hello, my name is {first_name} {last_name} and I am {age} years old.')
        
    dict_name = get_name()
    age = get_age()
    greet(first_name= dict_name['first_name'],
          last_name= dict_name['last_name'],
          age= age)        
    
dag_greet =  test_etl()    