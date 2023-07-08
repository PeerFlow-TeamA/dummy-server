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
    

class Question():
    def __init__(self, 
                id,
                title,
                content,
                nickname,
                password,
                views,
                recomment,
                created_at,
                updated_at):
        self.id : int = id
        self.title : str = title
        self.content : str = content
        self.nickname : str = nickname
        self.password : str = password
        self.views : int = views
        self.recomment : int = recomment
        self.created_at : str = created_at
        self.updated_at : str = updated_at

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "nickname": self.nickname,
            "password": self.password,
            "views": self.views,
            "recomment": self.recomment,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

class Answer():
    def __init__(self,
                id,
                question_id,
                content,
                nickname,
                password,
                recomment,
                isAdopted,
                created_at,
                updated_at):
        self.id : int = id
        self.question_id : int = question_id
        self.content : str = content
        self.nickname : str = nickname
        self.password : str = password
        self.recomment : int = recomment
        self.isAdopted : bool = isAdopted
        self.created_at : str = created_at
        self.updated_at : str = updated_at
    
    def to_dict(self):
        return {
            "id": self.id,
            "question_id": self.question_id,
            "content": self.content,
            "nickname": self.nickname,
            "password": self.password,
            "recomment": self.recomment,
            "isAdopted": self.isAdopted,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
class QuestionComment():
    def __init__(self,
                id,
                question_id,
                content,
                nickname,
                password,
                created_at,
                updated_at):
        self.id : int = id
        self.question_id : int = question_id
        self.content : str = content
        self.nickname : str = nickname
        self.password : str = password
        self.created_at : str = created_at
        self.updated_at : str = updated_at

    def to_dict(self):
        return {
            "id": self.id,
            "question_id": self.question_id,
            "content": self.content,
            "nickname": self.nickname,
            "password": self.password,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
class AnswerComment():
    def __init__(self,
                id,
                answer_id,
                content,
                nickname,
                password,
                created_at,
                updated_at):
        self.id : int = id
        self.answer_id : int = answer_id
        self.content : str = content
        self.nickname : str = nickname
        self.password : str = password
        self.created_at : str = created_at
        self.updated_at : str = updated_at

    def to_dict(self):
        return {
            "id": self.id,
            "answer_id": self.answer_id,
            "content": self.content,
            "nickname": self.nickname,
            "password": self.password,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
