from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


from .models import Update
# def detail_view(request):
# return render()  # return JSON --> JS Object Notation
# return HttpResponse(get_template().render({}))


def update_model_detail_view(request):
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    return JsonResponse(data)
