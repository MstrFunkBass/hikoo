from django.shortcuts import render
from django.http import HttpResponse
from .pythonscripts import haiku_gen


def index(request):
    haiku_gen.return_haiku()
    return HttpResponse("Hello, world. You're at the polls index.")
