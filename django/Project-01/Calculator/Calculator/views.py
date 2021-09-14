from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def result(request):
    expression = request.GET.get('numresult', '0')
    result = eval(expression)
    params = {'numresult':result}
    return render(request, 'result.html',params)