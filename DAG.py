import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from elasticsearch import Elasticsearch
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from dateutil import parser
import time

default_args= {
    'owner': 'Jyo',
    'start_date': datetime(2024, 11, 1)
}

with DAG(
    'etl_csv_files',
    description='from gdrive to postgres',
    schedule_interval='10,20,30 9 * * 6',
    default_args=default_args,
    catchup=False,
    start_date=datetime(2024, 11, 1)   # <-- Add this line
) as dag:
    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')


    @task()
    def insert_to_db():
        database = "airflow"
        username = "airflow"
        password = "airflow"
        host = "postgres"

        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

        engine = create_engine(postgres_url)
        conn = engine.connect()

        df = pd.read_sql("SELECT * FROM table_m3", conn)
        df.to_csv('/opt/airflow/data/P2M3_jyotis_sugata_data.csv', index=False)

        '''df = pd.read_csv('/opt/airflow/data/P2M3_jyotis_sugata_data_combine_preprocessed.csv')

        df.to_sql('data_customer', conn, index=False, if_exists='replace')
        print("Success INSERT")'''

        print('Success INSERT')

    @task()
    def preprocess_data():
        # Load data
        df = pd.read_csv('/opt/airflow/data/P2M3_jyotis_sugata_data.csv')

        # ================================
        # 1. Normalisasi Nama Kolom
        # ================================
        df.columns = (
            df.columns
            .str.strip()                 # hapus spasi/tab di awal/akhir
            .str.lower()                 # ubah jadi lowercase
            .str.replace(r'\s+', '_', regex=True)  # spasi → underscore
            .str.replace(r'[^a-z0-9_]', '', regex=True)  # hapus simbol selain huruf/angka/underscore
        )

        # ================================
        # 2. Handling Missing Values
        # ================================
        # Numeric: isi dengan mean
        df.fillna(df.mean(numeric_only=True), inplace=True)

        # Non-numeric: isi dengan 'unknown'
        for col in df.select_dtypes(include=['object']).columns:
            df[col].fillna('unknown', inplace=True)

        # ================================
        # 3. Hapus Data Duplikat
        # ================================
        df.drop_duplicates(inplace=True)

        # ================================
        # 4. Simpan Hasil Cleaning
        # ================================
        output_path = '/opt/airflow/data/P2M3_jyotis_sugata_data_clean.csv'
        df.to_csv(output_path, index=False)

        print("Success PREPROCESSING")
        print(f"Cleaned data saved to {output_path}")

    @task()
    def load_data():
        es = Elasticsearch("http://elasticsearch:9200")
        df = pd.read_csv('/opt/airflow/data/P2M3_jyotis_sugata_data_clean.csv')
        time.sleep(0.5)
        for i, row in df.iterrows():
            res = es.index(index="data_latihan", id=i+1, body=row.to_json())

start >> insert_to_db() >> preprocess_data() >> load_data() >> end