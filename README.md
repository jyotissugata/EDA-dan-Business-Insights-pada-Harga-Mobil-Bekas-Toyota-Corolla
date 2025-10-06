# Exploratory Data Analysis dan Business Insights pada Harga Mobil Bekas Toyota Corolla

## Repository Outline

- ddl.txt 
    - URL dataset yang dijadikan acuan.
    - Syntax DDL untuk pembuatan table.
    - Syntax DML untuk melakukan insert data ke database. Anda bisa menggunakan perintah COPY untuk melakukan insert data.
- data_raw.csv 
    - File ini berisi dataset original yang akan dimasukkan ke dalam database PostgreSQL.
- data_clean.csv 
    - File ini berisi data yang telah dilakukan Data Cleaning.
- DAG.py
    - File yang berisi DAG untuk dijalankan dengan menggunakan Apache Airflow yang terdiri dari :
        - Python code untuk mengambil data dari database PostgreSQL.
        - Python code untuk melakukan proses Data Cleaning seperti yang sudah ditentukan dan menyimpannya ke sebuah CSV file.
        - Python code untuk me-load CSV yang berisi data yang sudah clean dan memasukkannya ke dalam Elasticsearch.
- DAG_graph.jpg
    - Screenshot yang menampilkan alur graph dari DAG yang dibuat.
    - Jalankan penjadwalan yang Anda buat. Setelah selesai dilakukan, barulah screenshot graph DAG ini.
    - Alur graph DAG haruslah berwarna hijau pada semua task-nya yang menandakan tidak ada masalah pada proses penjadwalan.
- conceptual.txt
    - File ini berisi jawaban conceptual problem.
- GX.ipynb 
    - Notebook validasi data menggunakan Great Expectations
- /images
    - introduction & objective.png.
    - plot & insight 01.png.
    - plot & insight 02.png.
    - plot & insight 03.png.
    - plot & insight 04.png.
    - plot & insight 05.png.
    - plot & insight 06.png.
    - kesimpulan.png.
- README.md – Deskripsi project (file ini)

## Problem Background

Pasar mobil bekas semakin berkembang dengan meningkatnya kebutuhan konsumen terhadap kendaraan dengan harga terjangkau. Toyota Corolla merupakan salah satu model populer, namun variasi harga bergantung pada faktor-faktor seperti tahun produksi, kilometer tempuh, tenaga mesin (horsepower), warna, hingga jenis bahan bakar.

Project ini dilakukan untuk memahami pola data, memberikan rekomendasi bisnis yang dapat membantu dealer dalam menentukan strategi penjualan, serta mengoptimalkan segmentasi produk.

## Project Output

- Data yang sudah dibersihkan dari missing values, duplikat, dan inkonsistensi.
- Validasi data dengan Great Expectations untuk memastikan kualitas data.
- Dashboard Kibana yang berisi minimal 6 visualisasi + narasi insight.
- Rekomendasi bisnis berdasarkan hasil EDA.

## Data

- Sumber: Kaggle – Price of Used Toyota Corolla Cars
- Karakteristik:
    - Jumlah baris: 1436 data penjualan mobil
    - Jumlah kolom: 39 (Id, Model, Price, Age_08_04, Mfg_Month, Mfg_Year, KM, Fuel_type, HP, Met_Color, Color, Automatic, CC, Doors, Cylinders, Gears, Quarterly, Weight, Mfr_Guarantee, BOVAG_Guarantee, Guarantee_Period, ABS, Airbag_1, Airbag_2, Airco, Automatic_airco, Boardcomputer, CD_Player, Central_Lock, Powered_Windows, Power_Steering, Radio, Mistlamps, Sport_Model, Backseat_Divider, Metallic_Rim, Radio_cassette, Parking_Assistant, Tow_Bar)
    - Data numerik dan kategorikal
    - Terdapat missing values dan duplikasi yang ditangani pada tahap preprocessing

## Method

- ETL dengan Airflow → load data ke PostgreSQL → preprocessing → push ke Elasticsearch
- Data Cleaning → normalisasi nama kolom, handling missing values, remove duplicates
- Data Validation dengan Great Expectations (7 expectations)
- Exploratory Data Analysis (EDA) dengan visualisasi di Kibana
- Business Recommendation berdasarkan insight dari hasil eksplorasi

## Stacks

Bahasa: Python
Tools: Apache Airflow, PostgreSQL, Elasticsearch, Kibana
Library Python: pandas, sqlalchemy, great_expectations, matplotlib, seaborn

## Reference

- Dataset: Kaggle – [Price of Used Toyota Corolla Cars](https://www.kaggle.com/datasets/vishakhdapat/price-of-used-toyota-corolla-cars/data)
- Dokumentasi Great Expectations: https://greatexpectations.io/
- Panduan Kibana Visualization: https://www.elastic.co/guide/en/kibana

**Referensi tambahan:**
- [Basic Writing and Syntax on Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Contoh readme](https://github.com/fahmimnalfrzki/Swift-XRT-Automation)
- [Another example](https://github.com/sanggusti/final_bangkit) (**Must read**)
- [Additional reference](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)