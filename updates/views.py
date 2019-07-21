import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


from .models import Update
# def detail_view(request):
# return render()  # return JSON --> JS Object Notation
# return HttpResponse(get_template().render({}))


def json_example_view(request):
    '''
    URI -- for a REST API
    GET -- Retrieve
    '''
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    json_data = json.dumps(data)
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')
