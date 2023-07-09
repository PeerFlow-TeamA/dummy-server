from django.views.decorators.csrf import csrf_exempt
from .http_handler import *
from .data_pool import *
from .entity import *
from .env import *
from .exceptions import *
from .pageable import *

def C_DET_09_create_answer_comment(request, answer_id):
    try:
        body_params = json.loads(request.body.decode("utf-8"))
        content = body_params['content']
        nickname = body_params['nickname']
        password = body_params['password']
        created_at = body_params['created_at']

        found = get_datapool().get_by_id(get_datapool().ANSWER_LIST, answer_id)

        if found is None:
            raise AnswerNotFoundError()

        elem = AnswerComment(
            id = get_datapool().get_next_id(get_datapool().ANSWER_COMMENT_LIST),
            answer_id = answer_id,
            content = content,
            nickname = nickname,
            password = password,
            created_at = created_at,
            updated_at = None
        )

        get_datapool().ANSWER_COMMENT_LIST.append(elem)

        return normal_response_json({
            "message" : "comment on answer created successfully"
        }, 201)
    except AnswerNotFoundError as e:
        return error_response(HTTP_STATUS_CODE.NOT_FOUND, error_msg_key, answer_not_found_error_msg)
    except Exception as e:
        return error_response(HTTP_STATUS_CODE.INTERNAL_SERVER_ERROR, error_msg_key, "Error occured - " + str(e))

def C_DET_10_modify_answer_comment(request, answer_id, comment_id):
    try:
        body_params = json.loads(request.body.decode("utf-8"))
        content = body_params['content']
        nickname = body_params['nickname']
        password = body_params['password']
        created_at = body_params['created_at']

        found = get_datapool().get_by_id(get_datapool().ANSWER_LIST, answer_id)

        if found is None:
            raise AnswerNotFoundError()

        found = get_datapool().get_by_id(get_datapool().ANSWER_COMMENT_LIST, comment_id)

        if found is None:
            raise AnswerCommentNotFoundError()
        if found.password != password:
            raise PasswordIncorrectError()

        found.content = content
        found.nickname = nickname
        found.created_at = created_at

        return normal_response_json({
            "message" : "comment on answer modified successfully"
        })
    except AnswerNotFoundError as e:
        return error_response(HTTP_STATUS_CODE.NOT_FOUND, error_msg_key, answer_not_found_error_msg)
    except AnswerCommentNotFoundError as e:
        return error_response(HTTP_STATUS_CODE.NOT_FOUND, error_msg_key, answer_comment_not_found_error_msg)
    except PasswordIncorrectError as e:
        return error_response(HTTP_STATUS_CODE.FORBIDDEN, error_msg_key, password_incorrect_error_msg)
    except Exception as e:
        return error_response(HTTP_STATUS_CODE.INTERNAL_SERVER_ERROR, error_msg_key, "Error occured - " + str(e))

def C_DET_11_delete_answer_comment(request, answer_id, comment_id):
    try:
        body_params = json.loads(request.body.decode("utf-8"))
        password = body_params['password']

        found = get_datapool().get_by_id(get_datapool().ANSWER_LIST, answer_id)

        if found is None:
            raise AnswerNotFoundError()

        found = get_datapool().get_by_id(get_datapool().ANSWER_COMMENT_LIST, comment_id)

        if found is None:
            raise AnswerCommentNotFoundError()
        if found.password != password:
            raise PasswordIncorrectError()

        get_datapool().ANSWER_COMMENT_LIST.remove(found)

        return normal_response_json({
            "message" : "comment on answer deleted successfully"
        })
    except AnswerNotFoundError as e:
        return error_response(HTTP_STATUS_CODE.NOT_FOUND, error_msg_key, answer_not_found_error_msg)
    except AnswerCommentNotFoundError as e:
        return error_response(HTTP_STATUS_CODE.NOT_FOUND, error_msg_key, answer_comment_not_found_error_msg)
    except PasswordIncorrectError as e:
        return error_response(HTTP_STATUS_CODE.FORBIDDEN, error_msg_key, password_incorrect_error_msg)
    except Exception as e:
        return error_response(HTTP_STATUS_CODE.INTERNAL_SERVER_ERROR, error_msg_key, "Error occured - " + str(e))

def C_DET_12_get_all_of_comment_answer(request, answer_id):
    try:
        found = get_datapool().get_by_id(get_datapool().ANSWER_LIST, answer_id)
        query_params = get_query_params(request)
        page, size = int(query_params['page']), int(query_params['size'])

        if found is None:
            raise AnswerNotFoundError()
        
        comments = get_datapool().get_all_of_comment_answer(answer_id)

        if comments is None or len(comments) == 0:
            raise AnswerCommentNotFoundError()

        pageable = Pageable(comments, page, size, "views")
        return normal_response_json(pageable.to_dict())
    
    except AnswerNotFoundError as e:
        return error_response(HTTP_STATUS_CODE.NOT_FOUND, error_msg_key, answer_not_found_error_msg)
    except AnswerCommentNotFoundError as e:
        return error_response(HTTP_STATUS_CODE.NOT_FOUND, error_msg_key, answer_comment_not_found_error_msg)
    except Exception as e:
        return error_response(HTTP_STATUS_CODE.INTERNAL_SERVER_ERROR, error_msg_key, "Error occured - " + str(e))

@csrf_exempt
def C_DET_answer_comment_handler(request, answer_id = None, comment_id = None):
    if request.method == HTTP_METHOD.PUT and answer_id is not None and comment_id is not None:
        return C_DET_10_modify_answer_comment(request, answer_id, comment_id)
    if request.method == HTTP_METHOD.POST and answer_id is not None and comment_id is not None:
        return C_DET_11_delete_answer_comment(request, answer_id, comment_id)
    if request.method == HTTP_METHOD.GET and answer_id is not None:
        return C_DET_12_get_all_of_comment_answer(request, answer_id)
    if request.method == HTTP_METHOD.POST and answer_id is not None:
        return C_DET_09_create_answer_comment(request, answer_id)
    return not_allowed_method_response()
