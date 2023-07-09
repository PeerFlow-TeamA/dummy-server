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



class DataPool():
    def __init__(self) -> None:
        self.pool = {
            "writter_list" : [],
            "question_list" : [],
            "answer_list" : [],
            "question_comment_list" : [],
            "answer_comment_list" : []
        }
        self.QUESTION_LIST = self.pool["question_list"]
        self.ANSWER_LIST = self.pool["answer_list"]
        self.QUESTION_COMMENT_LIST = self.pool["question_comment_list"]
        self.ANSWER_COMMENT_LIST = self.pool["answer_comment_list"]
        self.WRITTER_LIST = self.pool["writter_list"]

    def set_writter_list(self, writter_list : list):
        self.pool["writter_list"] = writter_list

    def set_question_list(self, question_list : list):
        self.pool["question_list"] = question_list

    def set_answer_list(self, answer_list : list):
        self.pool["answer_list"] = answer_list

    def set_question_comment_list(self, question_comment_list : list):
        self.pool["question_comment_list"] = question_comment_list

    def set_answer_comment_list(self, answer_comment_list : list):
        self.pool["answer_comment_list"] = answer_comment_list

    def get_writter_list(self):
        return self.pool["writter_list"]
    
    def get_question_list(self):
        return self.pool["question_list"]
    
    def get_answer_list(self):
        return self.pool["answer_list"]
    
    def get_question_comment_list(self):
        return self.pool["question_comment_list"]
    
    def get_answer_comment_list(self):
        return self.pool["answer_comment_list"]
    
    def get_by_id(self, data : list, id : str):
        for item in data:
            if item.id == id:
                return item
        return None
    
    def replace(self, data : list, old_data : object, new_data : object):
        index = data.index(old_data)
        data[index] = new_data

    def delete(self, data : list, target : object):
        data.remove(target)

    def get_next_id(self, data : list):
        return len(data)

class InvalidPageError(Exception):
    pass

class DataCropper():
    @staticmethod
    def crop(data : list, start : int, end : int):
        size = len(data)
        if start < 0 or end < 0 or start > size or end > size:
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
    def search(data : list, search_keyword : str):
        result = []
        for item in data:
            if item.title.find(search_keyword) != -1:
                result.append(item)
        return result


class DataListSerializer():
    @staticmethod
    def convert(data : list):
        result = []
        for item in data:
            result.append(item.to_dict())
        return result


datapool = None
if datapool is None:
    datapool = DataPool()
    datapool.set_writter_list(read_writter_dummy(env.get("resource_dir") + env.get("writter_csv")))
    datapool.set_question_list(read_question_dummy(env.get("resource_dir") + env.get("question_csv")))

def get_datapool():
    return datapool