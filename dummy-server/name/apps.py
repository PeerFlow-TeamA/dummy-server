from django.apps import AppConfig
import subprocess
from .handlers import env
import os.path
from .handlers.data_pool import DataPool, read_writter_dummy, read_question_dummy, read_answer_dummy, read_question_comment_dummy, read_answer_comment_dummy

checkfileList = [
    'resource/question_data.csv',
    'resource/answer_data.csv',
    'resource/question_comment_data.csv',
    'resource/answer_comment_data.csv',
    'resource/writter_data.csv'
]

class DataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'name'

    def ready(self):
        print("DataConfig ready")
        # all check checkfileList exist
        if not all([os.path.isfile(checkfile) for checkfile in checkfileList]):
            subprocess.run(['python3', 'resource/dummy-data-generator/dummy_generator.py'])
            print("dummy data generated")
        else:
            print("dummy data already exists")
        
        # env check
        env.set("error_msg_key", "message")
        env.set("category_limit", ["minishell", "ft_irc", "minirt"])
        env.set("sort_limit", ["lastest", "views", "recommends"])
        env.set("resource_dir", "./resource/")
        env.set("question_csv", "question_data.csv")
        env.set("answer_csv", "answer_data.csv")
        env.set("question_comment_csv", "question_comment_data.csv")
        env.set("answer_comment_csv", "answer_comment_data.csv")
        env.set("writter_csv", "writter_data.csv")
        
        # env set
        env.set("question_csv_path", env.get("resource_dir") + env.get("question_csv"))
        env.set("answer_csv_path", env.get("resource_dir") + env.get("answer_csv"))
        env.set("question_comment_csv_path", env.get("resource_dir") + env.get("question_comment_csv"))
        env.set("answer_comment_csv_path", env.get("resource_dir") + env.get("answer_comment_csv"))
        env.set("writter_csv_path", env.get("resource_dir") + env.get("writter_csv"))

        DataPool.set_writter_list(read_writter_dummy(env.get("resource_dir") + env.get("writter_csv")))
        DataPool.set_question_list(read_question_dummy(env.get("resource_dir") + env.get("question_csv")))
        DataPool.set_answer_list(read_answer_dummy(env.get("resource_dir") + env.get("answer_csv")))
        DataPool.set_question_comment_list(read_question_comment_dummy(env.get("resource_dir") + env.get("question_comment_csv")))
        DataPool.set_answer_comment_list(read_answer_comment_dummy(env.get("resource_dir") + env.get("answer_comment_csv")))

        print("DataConfig ready end")
        pass