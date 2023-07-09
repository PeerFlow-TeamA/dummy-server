# csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from .http_handler import *
from .data_pool import *
from .entity import *
from .env import *
from .exceptions import *
import json

@request_only(HTTP_METHOD.POST)
def B_WRI_00_create_question(request):
    try:
        body_params = json.loads(request.body.decode("utf-8"))
        id = body_params['id']
        title = body_params['title']
        content = body_params['content']
        nickname = body_params['nickname']
        password = body_params['password']
        category = body_params['category']
        created_at = body_params['created_at']

        if category not in env.get("category_limit"):
            raise CategoryValueError(category)

        elem = Question(
            id = id,
            title = title,
            content = content,
            nickname = nickname,
            password = password,
            views = 0,
            recomment = 0,
            created_at = created_at,
            updated_at = None
        )

        DataPool.add(DataPool.QUESTION_LIST, elem)

        return normal_response_json({
            "message" : "question created successfully"
        })
    except CategoryValueError as e:
        return error_response(400, error_msg_key, category_value_error_msg)
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))

@request_only(HTTP_METHOD.PUT)
def B_WRI_01_modify_question(request):
    try:
        body_params = json.loads(request.body.decode("utf-8"))
        id = body_params['id']
        title = body_params['title']
        content = body_params['content']
        nickname = body_params['nickname']
        password = body_params['password']
        category = body_params['category']
        created_at = body_params['created_at']

        if category not in env.get("category_limit"):
            raise CategoryValueError(category)

        found = DataSearchEngine.search_by_id(DataPool.QUESTION_LIST, id)

        if found is None:
            raise QuestionNotFoundError()
        if found.password != password:
            raise PasswordIncorrectError()

        elem = Question(
            id = id,
            title = title,
            content = content,
            nickname = nickname,
            password = password,
            views = found.views,
            recomment = found.recomment,
            created_at = found.created_at,
            updated_at = created_at
        )

        DataPool.replace(DataPool.QUESTION_LIST, found, elem)

        return normal_response_json({
            "message" : "question modified successfully"
        }, 201)
    except CategoryValueError as e:
        return error_response(400, error_msg_key, category_value_error_msg)
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))

@request_only(HTTP_METHOD.POST)
def B_WRI_02_delete_question(request, question_id):
    try:
        body_params = json.loads(request.body.decode("utf-8"))

        found = DataSearchEngine.search_by_id(DataPool.QUESTION_LIST, question_id)
        if found is None:
            raise QuestionNotFoundError()
        if found.password != body_params['password']:
            raise PasswordIncorrectError()
        
        DataPool.delete(DataPool.QUESTION_LIST, found)
        
        return normal_response_json({
            "message" : "question modified successfully"
        })
    except QuestionNotFoundError as e:
        return error_response(404, error_msg_key, question_not_found_error_msg)
    except PasswordIncorrectError as e:
        return error_response(403, error_msg_key, password_incorrect_error_msg)
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))


@csrf_exempt
def B_WRI_question_handler(request, question_id = None):
    if request.method == HTTP_METHOD.POST and question_id is not None:
        return B_WRI_02_delete_question(request, question_id)
    
    if request.method == HTTP_METHOD.POST:
        return B_WRI_00_create_question(request)
    
    if request.method == HTTP_METHOD.PUT:
        return B_WRI_01_modify_question(request)
    
    return not_allowed_method_response()