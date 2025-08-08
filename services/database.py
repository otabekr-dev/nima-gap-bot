import json
from typing import Dict


class DB:

    def __init__(self, filename='data/db.json'):
        self.__filename = filename
        self.__data: Dict[str, Dict] = None
        self.__load()

    def __load(self):
        try:
            with open(self.__filename) as f:
                self.__data = json.load(f)
        except json.decoder.JSONDecodeError:
            self.__data = {
                "users": {},
                "feedback": {},
            }
        except FileNotFoundError:
            with open(self.__filename, 'x'):
                self.__data = {
                    "users": {},
                    "feedback": {},
                }

    def __save(self):
        with open(self.__filename, 'w') as f:
            json.dump(self.__data, f, indent=4)

    def create_user(self, chat_id: str):
        if self.get_user(chat_id) is None:
            self.__data['users'][str(chat_id)] = {}
            self.__save()

    def update_user(self, chat_id: str, data: dict):
        user = self.get_user(chat_id)
        if user is not None:
            self.__data['users'][str(chat_id)].update(data)
            self.__save()

    def get_user(self, chat_id: str):
        return self.__data['users'].get(str(chat_id))

    def get_data(self):
        return self.__data
