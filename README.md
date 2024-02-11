# Automatic People Detection and Tracking System Through CCTV using Face Recognition on Information Technology Department

This repository contains program from my simple undergraduate thesis

# Requirement
Following requirement is required:
## PostgreSQL Database
Create a new table named "face_data" to contain result from [notebook](https://github.com/dvjhr/CCTV-Tugas-Akhir/blob/master/insightface_reborn.ipynb)
```
CREATE TABLE face_data (
    id SERIAL PRIMARY KEY,
    path VARCHAR(255),
    embedding DOUBLE PRECISION[]
);
```
## Python Libraries
*Note that this only instal dependencies for website deployment, refer to notebook for more information regarding notebook's dependencies 
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
python sbadmin2.py
```

# Author 
Dava Aditya Jauhar\
05311940000030\
Information Technology Department\
Faculty of Intelligence Electrical and Informatics Technology\
Sepuluh Nopember Institute of Technology\