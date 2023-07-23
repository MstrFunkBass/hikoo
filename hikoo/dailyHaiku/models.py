from django.db import models
from .apps import OverwriteStorage
import os
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from hikoo.custom_azure import AzureMediaStorage


class Haiku(models.Model):
    haiku_id = models.AutoField(primary_key=True)
    line_one = models.CharField(max_length=100)
    line_two = models.CharField(max_length=100)
    line_three = models.CharField(max_length=100)
    date_created = models.DateTimeField("date published")
    label = 'haikuEntry'

class DalleImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_file = models.ImageField(storage= AzureMediaStorage, upload_to='background/', default='background/none-image.png', max_length=1000)
    image_url = models.URLField(max_length=1000)
    date_created = models.DateTimeField("date published")
    label = 'imageEntry'