from django.views.decorators.csrf import csrf_exempt
from .http_handler import *
from .data_pool import *
from .entity import *
from .env import *
from .exceptions import *


def C_DET_01_create_answer(request):
    try:
        body_params = json.loads(request.body.decode("utf-8"))
        id = body_params['id']
        question_id = body_params['question_id']
        content = body_params['content']
        nickname = body_params['nickname']
        password = body_params['password']
        created_at = body_params['created_at']

        found = get_datapool().get_question_by_id(question_id)

        if found is None:
            raise QuestionNotFoundError()

        elem = Answer(
            id = id,
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
        return error_response(400, error_msg_key, question_not_found_error_msg)
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))

def C_DET_answer_handler(request, question_id = None):
    if request.method == HTTP_METHOD.POST:
        return C_DET_01_create_answer(request)
    
    return not_allowed_method_response()