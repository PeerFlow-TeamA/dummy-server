from django.http import JsonResponse, HttpResponse
from .env import env
from .http_handler import *
from .data_pool import get_datapool, DataCropper, DataListSerializer
import json

error_msg_key = "message"
sort_value_error_msg = "sort standard incorrected - sort standard must be one of [lastest, views, recommends]"
category_value_error_msg = "category not correct - category must be one of [ft_irc, minishell, minirt]"

class SortValueError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
    
class CategoryValueError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

def get_query_params(request):
    result = {}
    for key in request.GET:
        result[key] = request.GET.get(key)
    return result

def normal_response_json(payload, status_code = 200, content_type = "application/json"):
    return HttpResponse(json.dumps(payload), content_type=content_type, status=status_code)

def A_MAI_00_handler(request):
    try:
        query_params = get_query_params(request)

        if query_params['category'] not in env.get("category_limit"):
            raise CategoryValueError(category_value_error_msg)
        if query_params['sort'] not in env.get("sort_limit"):
            raise SortValueError(sort_value_error_msg)
    except SortValueError as e:
        return error_response(400, error_msg_key, e.message)
    except CategoryValueError as e:
        return error_response(400, error_msg_key, e.message)
    except Exception as e:
        return error_response(400, error_msg_key, "Error occured - " + str(e))

    try:
        writters = get_datapool().get_writter_list()
        jsons = DataListSerializer.convert(writters)
        page = int(query_params['page'])
        size = int(query_params['size'])
        # cropped = DataCropper.crop_page(writters, page, size)
        


        return normal_response_json({
            "category": query_params['category'],
            "sort": query_params['sort'],
            "page": query_params['page'],
            "size": query_params['size'],
            "writters": jsons
        })
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))



def A_MAI_01_handler(request):
    try:
        query_params = get_query_params(request)

        if query_params['sort'] not in env.get("sort_limit"):
            raise SortValueError(sort_value_error_msg)
    except SortValueError as e:
        return error_response(400, error_msg_key, e.message)
    except Exception as e:
        return error_response(400, error_msg_key, "Error occured - " + str(e))
    

    try:
        return JsonResponse({
            "title": query_params['title'],
            "sort": query_params['sort'],
        })    
    except Exception as e:
        return error_response(500, error_msg_key, "Error occured - " + str(e))
