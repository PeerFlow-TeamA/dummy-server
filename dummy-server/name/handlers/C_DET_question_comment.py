from django.views.decorators.csrf import csrf_exempt
from .http_handler import *
from .data_pool import *
from .entity import *
from .env import *
from .exceptions import *

def C_DET_05_create_question_comment(request, question_id):
    try:
        body_params = json.loads(request.body.decode("utf-8"))
        content = body_params['content']
        nickname = body_params['nickname']
        password = body_params['password']
        created_at = body_params['created_at']

        found = get_datapool().get_by_id(get_datapool().QUESTION_LIST, question_id)

        if found is None:
            raise QuestionNotFoundError()

        elem = QuestionComment(
            id = get_datapool().get_next_id(get_datapool().QUESTION_COMMENT_LIST),
            question_id = question_id,
            content = content,
            nickname = nickname,
            password = password,
            created_at = created_at,
            updated_at = None
        )

        get_datapool().QUESTION_COMMENT_LIST.append(elem)

        return normal_response_json({
            "message" : "question comment created successfully"
        }, 201)
    except QuestionNotFoundError as e:
        return error_response(404, error_msg_key, question_not_found_error_msg)
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))

def C_DET_06_modify_question_comment(request, question_id, comment_id):
    try:
        body_params = json.loads(request.body.decode("utf-8"))
        content = body_params['content']
        nickname = body_params['nickname']
        password = body_params['password']
        created_at = body_params['created_at']

        found_question = get_datapool().get_by_id(get_datapool().QUESTION_LIST, question_id)
        found_comment = get_datapool().get_by_id(get_datapool().QUESTION_COMMENT_LIST, comment_id)

        if found_question is None:
            raise QuestionNotFoundError()
        if found_comment.password != password:
            raise PasswordIncorrectError()
        if found_comment is None:
            raise QuestionCommentNotFoundError()

        found_comment.content = content
        found_comment.nickname = nickname
        found_comment.updated_at = created_at


        return normal_response_json({
            "message" : "question comment modified successfully"
        })
    except QuestionNotFoundError as e:
        return error_response(404, error_msg_key, question_not_found_error_msg)
    except QuestionCommentNotFoundError as e:
        return error_response(404, error_msg_key, question_comment_not_found_error_msg)
    except PasswordIncorrectError as e:
        return error_response(403, error_msg_key, password_incorrect_error_msg)
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))
    
    

@csrf_exempt
def C_DET_question_comment_handler(request, question_id = None, comment_id = None):
    if request.method == HTTP_METHOD.POST and question_id is not None:
        return C_DET_05_create_question_comment(request, question_id)
    
    if request.method == HTTP_METHOD.PUT and question_id is not None and comment_id is not None:
        return C_DET_06_modify_question_comment(request, question_id, comment_id)
    return not_allowed_method_response()