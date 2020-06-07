from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def moduDeveloper_home(request):
    return HttpResponse("moduDeveloper page입니다.")
