import json

class Writter():
    def __init__(self, id, nickname, password):
        self.id : int = id
        self.nickname : str = nickname
        self.password : str = password
    
    def to_dict(self):
        return {
            "id": self.id,
            "nickname": self.nickname,
            "password": self.password
        }