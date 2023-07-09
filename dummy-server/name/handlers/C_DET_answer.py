from django.views.decorators.csrf import csrf_exempt
from .http_handler import *
from .data_pool import *
from .entity import *
from .env import *
from .exceptions import *


def C_DET_01_create_answer(request):
    try:
        body_params = json.loads(request.body.decode("utf-8"))
        question_id = body_params['question_id']
        content = body_params['content']
        nickname = body_params['nickname']
        password = body_params['password']
        created_at = body_params['created_at']

        found = get_datapool().get_question_by_id(question_id)

        if found is None:
            raise QuestionNotFoundError()

        elem = Answer(
            id = get_datapool().get_next_id(get_datapool().ANSWER_LIST),
            question_id = question_id,
            content = content,
            nickname = nickname,
            password = password,
            recomment = 0,
            isAdopted = False,
            created_at = created_at,
            updated_at = None
        )

        get_datapool().ANSWER_LIST.append(elem)

        return normal_response_json({
            "message" : "answer created successfully"
        })
    except QuestionNotFoundError as e:
        return error_response(404, error_msg_key, question_not_found_error_msg)
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))
    
def C_DET_02_modify_answer(request):
    try:
        body_params = json.loads(request.body.decode("utf-8"))
        question_id = body_params['question_id']
        content = body_params['content']
        nickname = body_params['nickname']
        password = body_params['password']
        created_at = body_params['created_at']

        found = get_datapool().get_question_by_id(question_id)

        if found is None:
            raise QuestionNotFoundError()
        if found.password != password:
            raise PasswordIncorrectError()

        elem = Answer(
            id = get_datapool().get_next_id(get_datapool().ANSWER_LIST),
            question_id = question_id,
            content = content,
            nickname = nickname,
            password = password,
            recomment = 0,
            isAdopted = False,
            created_at = found.created_at,
            updated_at = created_at
        )

        get_datapool().ANSWER_LIST.append(elem)

        return normal_response_json({
            "message" : "answer created successfully"
        }, 201)
    except QuestionNotFoundError as e:
        return error_response(404, error_msg_key, e.message)
    except PasswordIncorrectError as e:
        return error_response(403, error_msg_key, e.message)
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))
    
def C_DET_03_delete_answer(request, answer_id):
    try:
        body_params = json.loads(request.body.decode("utf-8"))
        password = body_params['password']


        found = get_datapool().get_by_id(get_datapool().ANSWER_LIST, answer_id)

        if found is None:
            raise AnswerNotFoundError()
        if found.password != password:
            raise PasswordIncorrectError()

        get_datapool().delete(get_datapool().ANSWER_LIST, found)

        return normal_response_json({
            "message" : "answer deleted successfully"
        })
    except PasswordIncorrectError as e:
        return error_response(403, error_msg_key, e.message)
    except AnswerNotFoundError as e:
        return error_response(404, error_msg_key, e.message)
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))

def C_DET_04_adopt_answer(request, answer_id):
    try:
        body_params = json.loads(request.body.decode("utf-8"))
        password = body_params['password']

        found = get_datapool().get_by_id(get_datapool().ANSWER_LIST, answer_id)
        parent_question = get_datapool().get_by_id(get_datapool().QUESTION_LIST, answer_id)

        if found is None:
            raise AnswerNotFoundError()
        if parent_question is None:
            raise QuestionNotFoundError()
        if parent_question.password != password:
            raise PasswordIncorrectError()

        found.isAdopted = True

        return normal_response_json({
            "message" : "answer adopted successfully"
        })
    except QuestionNotFoundError as e:
        return error_response(404, error_msg_key, e.message)
    except PasswordIncorrectError as e:
        return error_response(403, error_msg_key, e.message)
    except AnswerNotFoundError as e:
        return error_response(404, error_msg_key, e.message)
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))

@csrf_exempt
def C_DET_answer_handler(request, answer_id = None):
    if request.method == HTTP_METHOD.POST and answer_id is not None:
        return C_DET_03_delete_answer(request, answer_id)
    
    if request.method == HTTP_METHOD.POST:
        return C_DET_01_create_answer(request)
    
    if request.method == HTTP_METHOD.PUT:
        return C_DET_02_modify_answer(request, answer_id)
    
    if request.method == HTTP_METHOD.PATCH and answer_id is not None:
        return C_DET_04_adopt_answer(request, answer_id)

    return not_allowed_method_response()