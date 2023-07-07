
class writter():
    def __init__(self, id, nickname, password):
        self.id : int = id
        self.nickname : str = nickname
        self.password : str = password

    def __str__(self):
        return f"{self.id}, {self.nickname}, {self.password}"
    
    def __repr__(self):
        return f"{self.id}, {self.nickname}, {self.password}"

    def get_id(self):
        return self.id
    
    def get_nickname(self):
        return self.nickname
    
    def get_password(self):
        return self.password