from django.http import JsonResponse
from .env import env

def A_MAI_00_handler(request):
    category : str = request.GET.get("category")
    sort : str = request.GET.get("sort")
    page : int = request.GET.get("page")
    size : int = request.GET.get("size")
    
    if category == None:
        category = env.get_env("title")
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