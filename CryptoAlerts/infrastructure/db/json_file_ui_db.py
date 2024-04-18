import json
import os
from application.interfaces.user_interface import UserInterface

class JsonFileUserDb(UserInterface):
    def __init__(self, users_file='data/users.json'):
        self.users_file = users_file
        file_size_octet_db_user_json=0
        if os.path.exists(users_file) and os.path.getsize(users_file) > file_size_octet_db_user_json:
            with open(users_file, 'r') as f:
                self.users = json.load(f)
        else:
            self.users = {}

    def save_user(self, username, password):
        self.users[username] = password
        self._save_users()

    def get_user(self, username):
        return self.users.get(username)

    def _save_users(self):
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f)
