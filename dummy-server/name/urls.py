"""
URL configuration for name project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # A_MAI
    path("v1", views.A_MAI_00_handler),
    path("v1/search", views.A_MAI_01_handler),
    path("v1/question/<int:question_id>/comment/<int:comment_id>", views.C_DET_question_comment_handler),
    path("v1/question/<int:question_id>/comment", views.C_DET_question_comment_handler),
    path("v1/question/<int:question_id>", views.C_DET_question_handler),
    path("v1/question", views.B_WRI_question_handler),
    path("v1/answer", views.C_DET_answer_handler),
    path("v1/answer/<int:answer_id>/comment/<int:comment_id>", views.C_DET_answer_comment_handler),
    path("v1/answer/<int:answer_id>/comment", views.C_DET_answer_comment_handler),
    path("v1/answer/<int:question_id>", views.C_DET_answer_handler),



]

# API documentation
# url | method | description
# --- | ------ | -----------
# ... | A_MAI_apis | ...
# /v1 | GET | Get all questions
# /v1/search | GET | Search questions by title
# ... | B_WRI_apis | ...
# /v1/question | POST | Create a question
# /v1/question/{question_id} | PUT | modify a question by id
# /v1/question/{question_id} | POST | delete a question by id
# ... | C_DET_apis | ...
# /v1/question/{question_id} | GET | Get a question by id
# /v1/answer | POST | Create an answer


