from django.http import JsonResponse
from .env import env
from .http_handler import *

error_msg_key = "message"

def A_MAI_00_handler(request):
    category : str = request.GET.get("category")
    sort : str = request.GET.get("sort")
    page : int = request.GET.get("page")
    size : int = request.GET.get("size")

    category_value = ["minishell", "ft_irc", "minirt"]
    sort_value = ["lastest", "views", "recommends"]
    
    if category not in category_value:
        return error_response(400, error_msg_key, "category not correct - category must be one of [ft_irc, minishell, minirt]")
    if sort not in sort_value:
        return error_response(400, error_msg_key, "sort standard incorrected - sort standard must be one of [lastest, views, recommends]")
    

    
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