from flask import Flask
from flask import request
from flask_cors import CORS
from mongodb import MongoConnection
app = Flask(__name__)
CORS(app)
database = MongoConnection().getConnection()

@app.route("/mailbox", methods=["GET", "POST"])
def getMailBox():
    initialize()
    if request.method == "GET":
        return {
            "mail": "testing@mytempmail.com"
        }
    elif request.method == "POST":
        return {
            "mail": "testingCreate@mytempmail.com",
            "token": "simpleTokenCreatedTesting"
        }

def initialize():
    collection = database.get_collection("email_addresses")
    collection.insert_one({
        "userId": "445sa1185943g55",
        "email": "firstmail@mytempmail.com"
    })