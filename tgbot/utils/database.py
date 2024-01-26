import redis
import json
from telebot.types import Message

class Database:
    """
    A simple Redis-based database class for storing user data.

    Attributes:
    - db (redis.Redis): The Redis connection.

    Methods:
    - find_one(key: int) -> dict or None: Find a user by key and return the user data.
    - insert_one(message: Message) -> None: Insert a new user entry based on a Message object.
    - update(key: int, data: dict) -> None: Update an existing user entry with new data.
    """
    def __init__(self) -> None:
        """
        Initialize the Database instance with a Redis connection.
        """
        self.db = redis.Redis()
        self.db.ping()
    
    def find_one(self, key: int) -> dict or None:
        """
        Find a user by key and return the user data.

        Parameters:
        - key (int): The key to identify the user.

        Returns:
        dict or None: The user data if found, or None if the user does not exist.
        """
        data = self.db.get(str(key))
        if not data:
            return None
        else:
            return json.loads(data)

    def insert_one(self, message: Message) -> None:
        """
        Insert a new user entry based on a Message object.

        Parameters:
        - message (Message): The Message object containing user information.

        Returns:
        None
        """
        data = {
            "username": message.from_user.username
        }
        self.db.set(str(message.from_user.id), json.dumps(data))
    
    def update(self, key: int, data: dict) -> None:
        """
        Update an existing user entry with new data.

        Parameters:
        - key (int): The key to identify the user.
        - data (dict): The data to update in the user entry.

        Returns:
        None
        """
        user = json.loads(self.db.get(str(key)))
        updated_user = {
            **user,
            **data
        }
        self.db.set(str(key), json.dumps(updated_user))
