from django.shortcuts import render
from django.http import HttpResponse
from .pythonscripts import haiku_gen
from .models import Haiku
import datetime

def index(request):

    latest_haiku = Haiku.objects.all().filter(date_created__gte=datetime.date.today())

    if not latest_haiku:
        lines = haiku_gen.return_haiku()

        new_record = Haiku(line_one = lines[0],
                           line_two = lines[1],
                           line_three = lines[2],
                           date_created = datetime.datetime.now())
        new_record.save()

    else:
        latest_haiku_id = latest_haiku.values('haiku_id')[0]['haiku_id']
        haiku = Haiku.objects.get(haiku_id = latest_haiku_id)
        lines = [haiku.line_one, haiku.line_two, haiku.line_three]

    context = {"line_1": lines[0],
               "line_2": lines[1],
               "line_3": lines[2]
               }

    return render(request, "dailyHaiku/index.html", context)





# from .models import Question


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)