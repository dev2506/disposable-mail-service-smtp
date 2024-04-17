from pymongo import MongoClient
import certifi

#TODO: Fetch from env

class MongoConnection:
    mongoUrl = "mongodb+srv://dev-admin:Dev25062000@cluster0.6ukxabv.mongodb.net/?retryWrites=true&w=majority"
    database = None
    def __init__(self):
        client = MongoClient(self.mongoUrl)
        self.database = client.get_database("dis_mails_stage")

    def getConnection(self): 
        return self.database
