import redis
import json
from telebot.types import Message

# Create a connection
class Database:
    def __init__(self) -> None:
        self.db = redis.Redis()
        self.db.ping()
    
    def find_one(self, key:int):
        data = self.db.get(str(key))
        if not data:
            return None
        else:
            return json.loads(self.db.get(str(key)))


    def insert_one(self, message:Message):
        data = {
            "username": message.from_user.username
        }
        data = self.db.set(str(message.from_user.id), json.dumps(data))
        print(data)
    
    def update(self, key:int, data:dict):
        user = json.loads(self.db.get(str(key)))
        updated_user = {
            **user,
            **data
        }
        self.db.set(str(key), json.dumps(updated_user))