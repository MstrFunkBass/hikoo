from django.shortcuts import render
from django.http import HttpResponse
from .pythonscripts import haiku_gen


def index(request):
    lines = haiku_gen.return_haiku()

    haiku_output = '\n'.join(lines)

    context = {"line_1": lines[0],
               "line_2": lines[1],
               "line_3": lines[2]}

    return render(request, "dailyHaiku/index.html", context)
