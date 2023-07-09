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

        found = get_datapool().get_question_by_id(question_id)

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

@csrf_exempt
def C_DET_question_comment_handler(request, question_id = None):
    if request.method == HTTP_METHOD.GET and question_id is not None:
        return C_DET_05_create_question_comment(request, question_id)
    return not_allowed_method_response()