import pandas as pd
import random
from faker import Faker


# import dummy_variable.py
from dummy_variable import *

# random genarate date time as format "yyyy-MM-dd hh:mm:ss"
def random_datetime():
    year = random.randint(date_random_min['year'], date_random_max['year'])
    month = random.randint(date_random_min['month'], date_random_max['month'])
    day = random.randint(date_random_min['day'], date_random_max['day'])
    hour = random.randint(date_random_min['hour'], date_random_max['hour'])
    minute = random.randint(date_random_min['minute'], date_random_max['minute'])
    second = random.randint(date_random_min['second'], date_random_max['second'])
    return f'{year}-{month}-{day} {hour}:{minute}:{second}'

def get_faker(lang : str = 'ko_KR'):
    ret = Faker(locale=lang)
    return ret

def generate_sentence(lang : str = 'ko_KR'):
    faker = get_faker(lang)
    return faker.sentence()

def generate_text(lang : str = 'ko_KR', without_endl : bool = True):
    faker = get_faker(lang)
    if without_endl is True:
        return faker.text().replace('\n', '')
    return faker.text()

def save_as_csv(df, csv_name):
    df.to_csv(csv_dir + csv_name, index=False)

def process_data_by_panadas(dummy_data, csv_head, data_process_func):
    # 데이터프레임 생성
    df = pd.DataFrame(dummy_data, columns=csv_head)

    # 데이터 가공
    if data_process_func is not None:
        df = data_process_func(df)

    # nickname 기준 중복 제거
    df = df.drop_duplicates(subset=['nickname'], keep='first')
    return df

# 더미데이터 생성
def generate_name_data(size : int):
    dummy_data = []
    pk = -1
    for _ in range(size):
        pk += 1
        last_name_korean : str = random.choice(list(last_names.keys()))
        last_name_english : str = last_names[last_name_korean]
        random_name : str = random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 3))
        nickname : str = ''.join(random_name) + last_name_english
        password : str = "1234"
        dummy_data.append([pk, nickname, password])

    df = process_data_by_panadas(dummy_data, csv_head['writter'], None)
    save_as_csv(df, csv_name['writter'])
    return df

def generate_question_data(size : int, writter_data = None):
    dummy_data = []
    pk = -1
    for _ in range(size):
        pk += 1
        title : str = generate_sentence(generate_sentence_lang)
        content : str = generate_text(generate_text_lang)
        writter : list = random.choice(writter_data.values.tolist()) if writter_data is not None else random.choice(dummy_data)
        nickname : str = writter[0]
        password : str = writter[1]
        views : int = random.randint(views_min, views_max)
        recomment : int = random.randint(recomment_min, recomment_max)
        created_at : str = random_datetime()
        updated_at : str = random_datetime() if random.randint(0, 1) == 1 else 'NULL'
        dummy_data.append([pk, title, content, nickname, password, views, recomment, created_at, updated_at])

    df = process_data_by_panadas(dummy_data, csv_head['question'], None)
    save_as_csv(df, csv_name['question'])
    return df

def generate_answer_data(size : int, question_data = None, writter_data = None):
    dummy_data = []
    pk = -1
    for _ in range(size):
        pk += 1
        content : str = generate_text(generate_text_lang)
        question : list = random.choice(question_data.values.tolist()) if question_data is not None else random.choice(dummy_data)
        question_id : int = question[0]
        writter : list = random.choice(writter_data.values.tolist()) if writter_data is not None else random.choice(dummy_data)
        nickname : str = writter[0]
        password : str = writter[1]
        recomment : int = random.randint(recomment_min, recomment_max)
        isAdopted : int = random.randint(0, 1)
        created_at : str = random_datetime()
        updated_at : str = random_datetime() if random.randint(0, 1) == 1 else 'NULL'
        dummy_data.append([pk, question_id, content, nickname, password, recomment, isAdopted, created_at, updated_at])

    df = process_data_by_panadas(dummy_data, csv_head['answer'], None)
    save_as_csv(df, csv_name['answer'])
    return df

def generate_question_comment_data(size : int, question_data = None, writter_data = None):
    dummy_data = []
    pk = -1
    for _ in range(size):
        pk += 1
        content : str = generate_text(generate_text_lang)
        question : list = random.choice(question_data.values.tolist()) if question_data is not None else random.choice(dummy_data)
        question_id : int = question[0]
        writter : list = random.choice(writter_data.values.tolist()) if writter_data is not None else random.choice(dummy_data)
        nickname : str = writter[0]
        password : str = writter[1]
        created_at : str = random_datetime()
        updated_at : str = random_datetime() if random.randint(0, 1) == 1 else 'NULL'
        dummy_data.append([pk, question_id, content, nickname, password, created_at, updated_at])

    df = process_data_by_panadas(dummy_data, csv_head['question_comment'], None)
    save_as_csv(df, csv_name['question_comment'])
    return df
    

def generate_answer_comment_data(size : int, answer_data = None, writter_data = None):
    dummy_data = []
    pk = -1
    for _ in range(size):
        pk += 1
        content : str = generate_text(generate_text_lang)
        answer : list = random.choice(answer_data.values.tolist()) if answer_data is not None else random.choice(dummy_data)
        answer_id : int = answer[0]
        writter : list = random.choice(writter_data.values.tolist()) if writter_data is not None else random.choice(dummy_data)
        nickname : str = writter[0]
        password : str = writter[1]
        created_at : str = random_datetime()
        updated_at : str = random_datetime() if random.randint(0, 1) == 1 else 'NULL'
        dummy_data.append([pk, answer_id, content, nickname, password, created_at, updated_at])

    df = process_data_by_panadas(dummy_data, csv_head['answer_comment'], None)
    save_as_csv(df, csv_name['answer_comment'])
    return df

def generate():
    writter = generate_name_data(dummy_size['writter'])
    question = generate_question_data(dummy_size['question'], writter)
    answer = generate_answer_data(dummy_size['answer'], question, writter)
    question_comment = generate_question_comment_data(dummy_size['question_comment'], question, writter)
    answer_comment = generate_answer_comment_data(dummy_size['answer_comment'], answer, writter)

if __name__ == '__main__':
    generate()