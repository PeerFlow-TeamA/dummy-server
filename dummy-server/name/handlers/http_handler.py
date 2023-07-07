from django.http import JsonResponse

def error_response(status_code, message_key, message):
    return JsonResponse({
        message_key : message
    }, status=status_code)