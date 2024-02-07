#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
# from pymongo import MongoClient
import jinja2.exceptions

import psycopg2
from psycopg2 import sql

connection_params = {
    'host': 'localhost',
    'database': 'tugas_akhir',
    'user': 'postgres',
    'password': 'postgres',
}

conn = psycopg2.connect(**connection_params)

# Create a cursor
cursor = conn.cursor()

app = Flask(__name__)

def get_data_detail(name_input):
    name = name_input[0].replace(".jpg","").split("_")  
    print(name)
    return name

import numpy as np

def findCosineDistance(source_representation, test_representation):
    a = np.matmul(np.transpose(source_representation), test_representation)
    b = np.sum(np.multiply(source_representation, source_representation))
    c = np.sum(np.multiply(test_representation, test_representation))
    return 1 - (a / (np.sqrt(b) * np.sqrt(c)))

@app.route('/')
def index():
    insert_query = sql.SQL("SELECT path from face_data")
    # Execute the query
    all_data = []
    cursor.execute(insert_query)
    result = cursor.fetchall()
    # print(result)
    for i in result:
        cleaned = get_data_detail(i)
        all_data.append([cleaned[0], f"{cleaned[1]}/{cleaned[2]}/{cleaned[3]} {cleaned[4]}:{cleaned[5]}:{cleaned[6]}", cleaned[7], str(i[0])])
    return render_template('index.html', data=all_data)

@app.route('/detail/<base_path>')
def detail(base_path):
    insert_query_base = sql.SQL("SELECT id, embedding from face_data where path = %s")
    insert_query = sql.SQL("SELECT id, embedding from face_data")
    # Execute the query
    all_data = []
    cursor.execute(insert_query_base, (base_path,))
    result_base = cursor.fetchall()[0][1]
    # print("RESULT BASE", type(result_base))
    cursor.execute(insert_query)
    result_all = cursor.fetchall()
    final_result = []
    for data in result_all:
        # print(f"{data[0]}", type(data[1]))
        score_res = findCosineDistance(result_base, data[1])
        if score_res < 0.00001:
            print(score_res, "0.0")
            score_res = 0.0
        if score_res < 0.5:
            final_result.append((data[0], score_res))
        final_result.append((data[0], score_res))
    for ids, scores in final_result:
        get_data_sql = sql.SQL("SELECT path from face_data where id = %s")
        cursor.execute(get_data_sql, (ids,))
        my_res = cursor.fetchone()
        # print(my_res)
        cleaned = get_data_detail(my_res)
        # print(cleaned, my_res)
        all_data.append([cleaned[0], f"{cleaned[1]}/{cleaned[2]}/{cleaned[3]} {cleaned[4]}:{cleaned[5]}:{cleaned[6]}", cleaned[7], my_res[0], scores])
    # print(all_data)
    return render_template('detail.html', base_data=base_path, data=all_data)

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/<pagename>')
def admin(pagename):
    return render_template(pagename+'.html')

@app.errorhandler(jinja2.exceptions.TemplateNotFound)
def template_not_found(e):
    return not_found(e)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port="8008")
