from django.shortcuts import render
from django.http import HttpResponse
from .pythonscripts import haiku_gen, image_gen
from .models import Haiku, DalleImage
import datetime
import urllib.request
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from azure.storage.blob import BlobServiceClient
import environ

env = environ.Env()

environ.Env.read_env()

AZURE_STORAGE_ACCOUNT_NAME = "hikoodls"
STORAGE_ACCOUNT_KEY = env('AZURESTORAGEKEY')
CONTAINER_NAME = "media"
blob_name = "Background.png"
STORAGEACCOUNTURL= 'https://hikoodls.blob.core.windows.net'
CONTAINERNAME= 'media'
BLOBNAME= 'background/Background.png'

def index(request):

    latest_haiku = Haiku.objects.all().filter(date_created__gte=datetime.date.today())

    if not latest_haiku:

        blob_service_client = BlobServiceClient(account_url=STORAGEACCOUNTURL,credential=STORAGE_ACCOUNT_KEY)
        blob_client = blob_service_client.get_blob_client(container=CONTAINERNAME, blob=BLOBNAME)
        
        try:
            blob_client.delete_blob()
        except:
            pass

        lines = haiku_gen.return_haiku()

        new_record = Haiku(line_one = lines[0],
                           line_two = lines[1],
                           line_three = lines[2],
                           date_created = datetime.datetime.now())
        new_record.save()

        haiku_prompt = ', '.join(lines)

        image_url = image_gen.generate_image(haiku_prompt)

        new_image = DalleImage()
        
        new_image.image_url = image_url
        new_image.date_created = datetime.datetime.now()

        new_image.save()

        img_temp = NamedTemporaryFile()

        img_temp.write(urllib.request.urlopen(image_url).read())

        img_temp.flush()

        new_image.image_file.save("Background.png", File(img_temp))
      
        new_image.save()

    else:
        # latest_haiku_id = latest_haiku.values('haiku_id')[0]['haiku_id']
        latest_haiku_id = Haiku.objects.latest('haiku_id').haiku_id
        haiku = Haiku.objects.get(haiku_id = latest_haiku_id)
        lines = [haiku.line_one, haiku.line_two, haiku.line_three]


    latest_image_id = DalleImage.objects.latest('image_id').image_id
    image = DalleImage.objects.get(image_id = latest_image_id)
    
    context = {"line_1": lines[0],
               "line_2": lines[1],
               "line_3": lines[2],
               "date": datetime.date.today(),
               "image": image
               }

    return render(request, "dailyHaiku/index.html", context)
