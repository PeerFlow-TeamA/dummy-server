import csv
from .env import *
from .entity import *

def read_csv(file_path : str):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        return list(reader)

def read_writter_dummy(file_path : str):
    try:
        result = []
        writter_list = read_csv(file_path)[1:]
        for row in writter_list:
            result.append(Writter(row[0], row[1], row[2]))
    finally:
        return result
    
def read_question_dummy(file_path : str):
    try:
        result = []
        question_list = read_csv(file_path)[1:]
        for row in question_list:
            result.append(Question(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
    finally:
        return result
    
def read_answer_dummy(file_path : str):
    try:
        result = []
        answer_list = read_csv(file_path)[1:]
        for row in answer_list:
            result.append(Answer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    finally:
        return result
    
def read_question_comment_dummy(file_path : str):
    try:
        result = []
        question_comment_list = read_csv(file_path)[1:]
        for row in question_comment_list:
            result.append(QuestionComment(row[0], row[1], row[2], row[3], row[4]))
    finally:
        return result
    
def read_answer_comment_dummy(file_path : str):
    try:
        result = []
        answer_comment_list = read_csv(file_path)[1:]
        for row in answer_comment_list:
            result.append(AnswerComment(row[0], row[1], row[2], row[3], row[4]))
    finally:
        return result



class DataPool():
    pool = {
        "writter_list" : [],
        "question_list" : [],
        "answer_list" : [],
        "question_comment_list" : [],
        "answer_comment_list" : []
    }
    QUESTION_LIST = pool["question_list"]
    ANSWER_LIST = pool["answer_list"]
    QUESTION_COMMENT_LIST = pool["question_comment_list"]
    ANSWER_COMMENT_LIST = pool["answer_comment_list"]
    WRITTER_LIST = pool["writter_list"]

    @classmethod
    def set_writter_list(cls, writter_list : list):
        cls.pool["writter_list"] = writter_list        

    @classmethod
    def set_question_list(cls, question_list : list):
        cls.pool["question_list"] = question_list

    @classmethod
    def set_answer_list(cls, answer_list : list):
        cls.pool["answer_list"] = answer_list

    @classmethod
    def set_question_comment_list(cls, question_comment_list : list):
        cls.pool["question_comment_list"] = question_comment_list

    @classmethod
    def set_answer_comment_list(cls, answer_comment_list : list):
        cls.pool["answer_comment_list"] = answer_comment_list
    
    @classmethod
    def add(cls, data : list, new_data : object):
        data.append(new_data)

    @classmethod
    def replace(cls, data : list, old_data : object, new_data : object):
        index = data.index(old_data)
        data[index] = new_data

    @classmethod
    def delete(cls, data : list, target : object):
        data.remove(target)

    @classmethod
    def get_next_id(cls, data : list):
        return len(data)
    
    @staticmethod
    def replace(cls, data : list, old_data : object, new_data : object):
        index = data.index(old_data)
        data[index] = new_data


class InvalidPageError(Exception):
    pass

class DataCropper():
    @staticmethod
    def crop(data : list, start : int, end : int):
        size = len(data)
        if end < 0 or start > size:
            raise InvalidPageError
        return data[start:end]
    
    # 0번 페이지부터 지원
    @staticmethod
    def crop_page(data : list, page : int, page_size : int):
        start = page * page_size
        end = start + page_size
        return DataCropper.crop(data, start, end)

class DataSearchEngine():
    @staticmethod
    def search_by_title(data : list, search_title : str):
        result = []
        for item in data:
            if item.title.find(search_title) != -1:
                result.append(item)
        return result
    
    @staticmethod
    def search_by_id(data : list, id : int):
        for item in data:
            if item.id == id:
                return item
        return None

    @staticmethod
    def search_by_category(data : list, category : str):
        return list(filter(lambda x : x.category == category, data))

    @staticmethod
    def search_all_comments_on_question(question_id : int):
        return list(filter(lambda x : x.question_id == question_id, DataPool.QUESTION_COMMENT_LIST))

    @staticmethod
    def search_all_comments_on_answer(answer_id : int):
        return list(filter(lambda x : x.answer_id == answer_id, DataPool.ANSWER_COMMENT_LIST))

class DataListSerializer():
    @staticmethod
    def convert(data : list):
        result = []
        for item in data:
            result.append(item.to_dict())
        return result
