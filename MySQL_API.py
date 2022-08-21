from flask import Flask, request, jsonify
from flask import Flask,jsonify,request,make_response,url_for,redirect
#import requests, json

app = Flask(__name__)
db = MySQLdb.connect("localhost", "root", "mysqladmin")
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Open database connection
cursor.execute("Create database if not exists API_test")
cursor.execute("create table if not exists API_test.MySQLtable")




@app.route('/select',methods = ['GET','POST'])

def Select():
    if(request.method=='POST'):
        import MySQLdb

        sql = "SELECT * FROM candystore.employees;"

        # execute SQL query using execute() method.
        cursor.execute(sql)

        db.commit()

        # get the record count updated
        #print(cursor.rowcount, " record(s) affected")
        #print(cursor)

        # disconnect from server
        db.close()
        print (cursor.content)
        return cursor.content

if __name__=='__main__' :
    app.run()