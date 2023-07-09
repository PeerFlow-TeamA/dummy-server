from django.views.decorators.csrf import csrf_exempt
from .http_handler import *
from .data_pool import *
from .entity import *
from .env import *
from .exceptions import *
from .pageable import *

def C_DET_05_create_question_comment(request, question_id):
    try:
        body_params = json.loads(request.body.decode("utf-8"))
        found = DataSearchEngine.search_by_id(DataPool.QUESTION_LIST, question_id)

        if found is None:
            raise QuestionNotFoundError()

        elem = QuestionComment(
            id = DataPool.get_next_id(DataPool.QUESTION_COMMENT_LIST),
            question_id = question_id,
            content = body_params['content'],
            nickname = body_params['nickname'],
            password = body_params['password'],
            created_at = body_params['created_at'],
            updated_at = None
        )

        DataPool.add(DataPool.QUESTION_COMMENT_LIST, elem)

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

        found_question = DataSearchEngine.search_by_id(DataPool.QUESTION_LIST, question_id)
        found_comment = DataSearchEngine.search_by_id(DataPool.QUESTION_COMMENT_LIST, comment_id)

        if found_question is None:
            raise QuestionNotFoundError()
        if found_comment is None:
            raise QuestionCommentNotFoundError()
        if found_comment.password != body_params['password']:
            raise PasswordIncorrectError()
        
        elem = QuestionComment(
            id = DataPool.get_next_id(DataPool.QUESTION_COMMENT_LIST),
            question_id = question_id,
            content = body_params['content'],
            nickname = body_params['nickname'],
            password = body_params['password'],
            created_at = found_comment.created_at,
            updated_at = body_params['created_at']
        )

        DataPool.replace(DataPool.QUESTION_COMMENT_LIST, found_comment, elem)

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
    
def C_DET_07_delete_question_comment(request, question_id, comment_id):
    try:
        body_params = json.loads(request.body.decode("utf-8"))

        found_question = DataSearchEngine.search_by_id(DataPool.QUESTION_LIST, question_id)
        found_comment = DataSearchEngine.search_by_id(DataPool.QUESTION_COMMENT_LIST, comment_id)

        if found_question is None:
            raise QuestionNotFoundError()
        if found_comment is None:
            raise QuestionCommentNotFoundError()
        if found_comment.password != body_params['password']:
            raise PasswordIncorrectError()

        DataPool.delete(DataPool.QUESTION_COMMENT_LIST, found_comment)

        return normal_response_json({
            "message" : "question comment deleted successfully"
        })
    except QuestionNotFoundError as e:
        return error_response(404, error_msg_key, question_not_found_error_msg)
    except QuestionCommentNotFoundError as e:
        return error_response(404, error_msg_key, question_comment_not_found_error_msg)
    except PasswordIncorrectError as e:
        return error_response(403, error_msg_key, password_incorrect_error_msg)
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))

def C_DET_08_get_all_of_comment_by_question_id(request, question_id):
    try:
        query_params = get_query_params(request)
        page, size = int(query_params['page']), int(query_params['size'])

        found_question = DataSearchEngine.search_by_id(DataPool.QUESTION_LIST, question_id)
        found_comments = DataSearchEngine.search_by_question_id(DataPool.QUESTION_COMMENT_LIST, question_id)
        
        if found_question is None:
            raise QuestionNotFoundError()
        
        cropped = DataCropper(found_comments, page, size)
        sort = "views"
        pageable = Pageable(cropped, page, size, sort)

        return normal_response_json(pageable.to_dict())
    except QuestionNotFoundError as e:
        return error_response(404, error_msg_key, question_not_found_error_msg)
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))

@csrf_exempt
def C_DET_question_comment_handler(request, question_id = None, comment_id = None):
    if request.method == HTTP_METHOD.POST and question_id is not None:
        return C_DET_05_create_question_comment(request, question_id)
    
    if request.method == HTTP_METHOD.PUT and question_id is not None and comment_id is not None:
        return C_DET_06_modify_question_comment(request, question_id, comment_id)
    
    if request.method == HTTP_METHOD.POST and question_id is not None and comment_id is not None:
        return C_DET_07_delete_question_comment(request, question_id, comment_id)
    
    if request.method == HTTP_METHOD.GET and question_id is not None:
        return C_DET_08_get_all_of_comment_by_question_id(request, question_id)
    return not_allowed_method_response()