from django.db import models

class Haiku(models.Model):
    haiku_id = models.AutoField(primary_key=True)
    line_one = models.CharField(max_length=100)
    line_two = models.CharField(max_length=100)
    line_three = models.CharField(max_length=100)
    date_created = models.DateTimeField("date published")
    label = 'haikuEntry'