from django.views.decorators.csrf import csrf_exempt
from .http_handler import *
from .data_pool import *
from .entity import *
from .env import *
from .exceptions import *

@request_only(HTTP_METHOD.GET)
def C_DET_00_get_question_detail(request, question_id):
    try:
        body_params = json.loads(request.body.decode("utf-8"))\

        found_question : Question = DataSearchEngine.search_by_id(DataPool.QUESTION_LIST, question_id)
        if found_question is None:
            raise QuestionNotFoundError()
        if found_question.password != body_params['password']:
            raise PasswordIncorrectError()

        found_comments : list = DataSearchEngine.search_by_question_id(DataPool.ANSWER_LIST, question_id)
        

        response = {
            "nickname" : found_question.nickname,
            "content" : found_question.content,
            "created_at" : found_question.created_at,
            "updated_at" : found_question.updated_at,
            "answerList" : [comment.to_dict() for comment in found_comments],
            "type" : "question",
            "title" : found_question.title,
            "category" : found_question.category,
            "recommend" : found_question.recommend,
            "view" : found_question.view,
        }        

        return normal_response_json(response, 200)
    except QuestionNotFoundError as e:
        return error_response(400, error_msg_key, question_not_found_error_msg)
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))

@csrf_exempt
def C_DET_question_handler(request, question_id = None):

    # url : /question/<question_id>
    if request.method == HTTP_METHOD.GET and question_id is not None:
        return C_DET_00_get_question_detail(request, question_id)
    
    return not_allowed_method_response()