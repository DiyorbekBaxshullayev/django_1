from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest, HttpResponse, JsonResponse

def home(request: HttpRequest) ->HttpResponse:
    return HttpResponse('<h1>Hello</h1>')

def get_params(request: HttpRequest):
    params = request.GET
    number = params.get('number')
    print(number)

def get_sum(request: HttpRequest):
    params = request.GET

    a = params.get('a', 0)
    b = params.get('b', 0)

    result = {
        'result': int(a) + int(b)
    }

    return JsonResponse(result)
