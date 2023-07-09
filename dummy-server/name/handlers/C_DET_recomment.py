from django.views.decorators.csrf import csrf_exempt
from .http_handler import *
from .data_pool import *
from .entity import *
from .env import *
from .exceptions import *

def C_DET_13_recomment_question(request, question_id):
    try:
        found = DataSearchEngine.search_by_id(DataPool.QUESTION_LIST, question_id)

        if found is None:
            raise QuestionNotFoundError()
        
        found.recomment += 1

        return normal_response_json({
            "message" : "question recommented successfully"
        })
    except QuestionNotFoundError as e:
        return error_response(400, error_msg_key, question_not_found_error_msg)
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))


def C_DET_14_recomment_answer(request, answer_id):
    try:
        found = DataSearchEngine.search_by_id(DataPool.ANSWER_LIST, answer_id)

        if found is None:
            raise AnswerNotFoundError()
        
        found.recomment += 1

        return normal_response_json({
            "message" : "answer recommented successfully"
        })
    except AnswerNotFoundError as e:
        return error_response(400, error_msg_key, answer_not_found_error_msg)
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))

@csrf_exempt
def C_DET_recommentation_handler(request, question_id = None, answer_id = None):
    # url : /question/<int:question_id>/recomment
    if request.method == HTTP_METHOD.POST and question_id is not None:
        return C_DET_13_recomment_question(request, question_id)
    
    # url : /answer/<int:answer_id>/recomment
    if request.method == HTTP_METHOD.POST and answer_id is not None:
        return C_DET_14_recomment_answer(request, answer_id)
    
    return not_allowed_method_response()