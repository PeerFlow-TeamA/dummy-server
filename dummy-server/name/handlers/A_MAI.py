from django.http import JsonResponse, HttpResponse
from .env import env
from .http_handler import *
from .data_pool import get_datapool, DataCropper, DataListSerializer, DataSearchEngine
from .pageable import Pageable
from .exceptions import *
import json

def A_MAI_00_handler(request):
    try:
        if request.method != HTTP_METHOD.GET:
            return not_allowed_method_response()
        query_params = get_query_params(request)

        if query_params['category'] not in env.get("category_limit"):
            raise CategoryValueError()
        if query_params['sort'] not in env.get("sort_limit"):
            raise SortValueError()
    except SortValueError as e:
        return error_response(400, error_msg_key, e.message)
    except CategoryValueError as e:
        return error_response(400, error_msg_key, e.message)
    except Exception as e:
        return error_response(400, error_msg_key, "Error occured - " + str(e))

    try:
        questions = get_datapool().get_question_list()
        page, size = int(query_params['page']), int(query_params['size'])
        cropper = DataCropper.crop_page(questions, page, size)
        pageable = Pageable(cropper, page, size, query_params['sort'])
        return normal_response_json(pageable.to_dict())
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))


def A_MAI_01_handler(request):
    try:
        if request.method != HTTP_METHOD.GET:
            return not_allowed_method_response()
        query_params = get_query_params(request)
        if query_params['sort'] not in env.get("sort_limit"):
            raise SortValueError()
    except SortValueError as e:
        return error_response(400, error_msg_key, e.message)
    except Exception as e:
        return error_response(400, error_msg_key, "Error occured - " + str(e))

    try:
        questions = get_datapool().get_question_list()
        founds = DataSearchEngine.search(questions, query_params['title'])
        pageable = Pageable(founds, query_params['sort'])
        return normal_response_json(pageable.to_dict())
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))