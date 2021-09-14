from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    expression = request.GET.get('numresult', 'default')
    params = {'result': None}
    if expression != "default":
        params['result'] = eval(expression)
    return render(request, 'index.html', params)
