from django.http import JsonResponse
from django.http import HttpResponse
import json

class HTTP_METHOD():
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"

class HTTP_STATUS_CODE():
    # 2xx
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    # 4xx
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    # 5xx
    INTERNAL_SERVER_ERROR = 500

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

def not_allowed_method_response():
    return error_response(405, "message", "not allowed method")

# use this function as decorator for http handler
#  as example:
#  @request_only(HTTP_METHOD.GET)
#  def handler(request):
#      return normal_response_json({
#          "message" : "hello world"
#      })
def request_only(method):
    def impl(func):
        def wrapper(request):
            if request.method != method:
                return not_allowed_method_response()
            return func(request)
        return wrapper
    return impl