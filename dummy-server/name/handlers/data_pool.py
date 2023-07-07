import csv
from .entity import writter
from .env import *
import subprocess

def read_csv(file_path : str):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        return list(reader)

def read_writter_dummy(file_path : str):
    writter_list = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            temp_writter = writter(row[0], row[1], row[2])
            writter_list.append(temp_writter)
    return writter_list

class DataPool():
    def __init__(self) -> None:
        self.writter_list = []
        self.question_list = []
        self.answer_list = []
        self.question_comment_list = []
        self.answer_comment_list = []
        pass

    def set_writter_list(self, writter_list : list):
        self.writter_list = writter_list
    
    def set_question_list(self, question_list : list):
        self.question_list = question_list

    def set_answer_list(self, answer_list : list):
        self.answer_list = answer_list

    def set_question_comment_list(self, question_comment_list : list):
        self.question_comment_list = question_comment_list

    def set_answer_comment_list(self, answer_comment_list : list):
        self.answer_comment_list = answer_comment_list

    def get_writter_list(self):
        return self.writter_list

    def get_question_list(self):
        return self.question_list

    def get_answer_list(self):
        return self.answer_list

    def get_question_comment_list(self):
        return self.question_comment_list

    def get_answer_comment_list(self):
        return self.answer_comment_list

class DataCropper():
    @staticmethod
    def crop(data : list, start : int, end : int):
        return data[start:end]
    
    # 0번 페이지부터 지원
    @staticmethod
    def crop_page(data : list, page : int, page_size : int):
        start = page * page_size
        end = start + page_size
        return DataCropper.crop(data, start, end)
    

# 싱글톤 패턴 지원
datapool = None
if datapool is None:
    datapool = DataPool()

def get_datapool():
    return datapool


def init_datapool():
    datapool.set_writter_list(read_writter_dummy(env.get("resource_dir") + env.get("writter_csv")))