import csv
from .entity import writter

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