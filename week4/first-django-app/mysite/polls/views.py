# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def rutroh(request):
    return HttpResponse("<h1>I'm <span style='color:red;'>EXCITED</span> about Django!</h1>")
