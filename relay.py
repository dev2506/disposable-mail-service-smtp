from slimta.relay import Relay
from mongodb import MongoConnection
import math
import mailparser

# database = MongoConnection().getConnection()

class MessageRelay(Relay):
    def __init__(self):
        super().__init__()
    
    def attempt(self, envelope, attempts):
            print(f"-------Envelope Message--------- {envelope.message}")
            # messagesColl = database.get_collection("messages")
            # messagesColl.insert_one({
            #     "sender": envelope.sender,
            #     "timestamp": math.ceil(envelope.timestamp),
            #     "message": envelope.message.decode("utf-8").strip(),
            #     "recipients": envelope.recipients
            # })
