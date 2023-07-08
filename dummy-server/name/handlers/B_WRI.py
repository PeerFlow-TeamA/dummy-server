# csrf_exempt
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def B_WRI_00_handler(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category = request.POST.get("category")
        author = request.POST.get("author")
        
        
        return JsonResponse({
            "title": title,
            "content": content,
            "category": category,
            "author": author,
        })