from django.shortcuts import render
from django.http import HttpResponse
from .pythonscripts import haiku_gen


def index(request):
    lines = haiku_gen.return_haiku()

    haiku_output = '\n'.join(lines)

    return HttpResponse(haiku_output)
