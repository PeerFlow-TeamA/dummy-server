from django.http import JsonResponse
from .env import env
from .http_handler import *

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

def A_MAI_00_handler(request):
    try:
        category : str = request.GET.get("category")
        sort : str = request.GET.get("sort")
        page : int = int(request.GET.get("page"))
        size : int = int(request.GET.get("size"))
        
        if category not in env.get("category_limit"):
            raise CategoryValueError(category_value_error_msg)
        if sort not in env.get("sort_limit"):
            raise SortValueError(sort_value_error_msg)
    except SortValueError as e:
        return error_response(400, error_msg_key, e.message)
    except CategoryValueError as e:
        return error_response(400, error_msg_key, e.message)
    except Exception as e:
        return error_response(400, error_msg_key, "Error occured - " + str(e))

    print(category, sort, page, size)
    print(type(category), type(sort), type(page), type(size))

    return JsonResponse({
        "category": category,
        "sort": sort,
        "page": page,
        "size": size,
    })

def A_MAI_01_handler(request):
    category : str = request.GET.get("title")
    sort : str = request.GET.get("sort")
    
    return JsonResponse({
        "title": category,
        "sort": sort
    })