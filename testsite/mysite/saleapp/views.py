from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def catalog(request):
    return render(request, 'catalog.html')

def calc(request):
    return render(request, 'calculator.html')