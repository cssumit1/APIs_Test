from flask import Flask, request, jsonify
# pip install mysqlclient

from flask import Flask,jsonify,request,make_response,url_for,redirect
import mysql.connector as conn
#import requests, json

app = Flask(__name__)
mydb = conn.connect(host = "localhost", user = "root", passwd = "mysqladmin")
# prepare a cursor object using cursor() method
cursor = mydb.cursor()
# Open database connection
cursor.execute("Create database if not exists API_test")
cursor.execute("create table if not exists API_test.MySQLtable (name varchar(30) , number int)")

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into API_test.MySQLtable  values(%s , %s)", (name, number))
        mydb.commit()
        return jsonify(str('Successfully inserted'))

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        get_name = request.json['get_name']
        cursor.execute("Update API_test.MySQLtable set number = number+2222 where name = %s ", (get_name,))
        mydb.commit()
        return jsonify(str('Successfully Updated'))

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        get_name = request.json['get_name']
        cursor.execute("delete from API_test.MySQLtable where name = %s ", (get_name,))
        mydb.commit()
        return jsonify(str('Record Deleted.'))

@app.route('/select', methods=['POST'])
def select():
    if request.method == 'POST':
        get_name = request.json['get_name']
        cursor.execute("Update API_test.MySQLtable set number = number+2222 where name = %s ", (get_name,))
        mydb.commit()
        return jsonify(str('Successfully Updated'))

@app.route("/select", methods=['POST', 'GET'])
def fetch_data():
    cursor.execute("select * from API_test.MySQLtable")
    l = []
    for i in cursor.fetchall():
        l.append(i)
        return jsonify(str(l))

if __name__ == '__main__':
    app.run()