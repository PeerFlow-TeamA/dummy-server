from django.apps import AppConfig
import subprocess
from .handlers import env
import os.path

class DataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'name'

    def ready(self):
        print("DataConfig ready")
        if os.path.exists('resource/question_data.csv') == False:
            subprocess.run(['python3', 'resource/dummy-data-generator/dummy_generator.py'])
            print("dummy data generated")
        else:
            print("dummy data already exists")
        print("DataConfig ready end")
        pass