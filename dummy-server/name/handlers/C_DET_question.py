from django.views.decorators.csrf import csrf_exempt
from .http_handler import *
from .data_pool import *
from .entity import *
from .env import *
from .exceptions import *

def C_DET_00_get_question_detail(request, question_id):
    try:
        body_params = json.loads(request.body.decode("utf-8"))
        password = body_params['password']
        
        found = get_datapool().get_question_by_id(question_id)

        if found is None:
            raise QuestionNotFoundError()
        if found.password != password:
            raise PasswordIncorrectError()

        get_datapool().QUESTION_LIST.remove(found)

        return normal_response_json({
            "message" : "question deleted successfully"
        })
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