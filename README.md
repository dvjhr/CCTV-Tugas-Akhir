# Automatic People Detection and Tracking System Through CCTV using Face Recognition on Information Technology Department

This repository contains program from my simple undergraduate thesis dashboard, go to [here](https://github.com/dvjhr/CCTV-Tugas-Akhir-Model) for model's code

# Requirement
Following requirement is required:
1) PostgreSQL Database
- Download from its [official site](https://www.postgresql.org/)
- Create new database for example: 
```
CREATE DATABASE tugas_akhir WITH ENCODING 'UTF8' LC_COLLATE='English_United Kingdom' LC_CTYPE='English_United Kingdom';
```
- Create a new table named "face_data" to contain result from [notebook](https://github.com/dvjhr/CCTV-Tugas-Akhir/blob/master/insightface_reborn.ipynb)
```
CREATE TABLE face_data (
    id SERIAL PRIMARY KEY,
    path VARCHAR(255),
    embedding DOUBLE PRECISION[]
);
```
2) Python Libraries\
```
flask
numpy
psycopg2
```
or you can install using 
```
pip install requirements.txt
```

# Running Program

```
git clone https://github.com/dvjhr/CCTV-Tugas-Akhir.git
cd CCTV-Tugas-Akhir
python server.py
```

# Author 
Dava Aditya Jauhar\
05311940000030\
Information Technology Department\
Faculty of Intelligence Electrical and Informatics Technology\
Sepuluh Nopember Institute of Technology