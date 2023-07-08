from django.http import JsonResponse
from django.http import HttpResponse
import json

def error_response(status_code, message_key, message):
    return JsonResponse({
        message_key : message
    }, status=status_code)

def get_query_params(request):
    result = {}
    for key in request.GET:
        result[key] = request.GET.get(key)
    return result

def normal_response_json(payload, status_code = 200, content_type = "application/json"):
    return HttpResponse(json.dumps(payload), content_type=content_type, status=status_code)
