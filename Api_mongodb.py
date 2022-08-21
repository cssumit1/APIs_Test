
from flask import Flask,jsonify,request,make_response,url_for,redirect
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://##admin##:passwd#2321@ineuron.raxmhn5.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client["Api_testdb"]
collections = database ['mycollection']

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json["name"]
        number = request.json["number"]
        collections.insert_one({name:number})
        return jsonify(str("Successfully Inserted."))