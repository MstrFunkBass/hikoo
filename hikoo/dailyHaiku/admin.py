from django.contrib import admin

# Register your models here.

from .models import DalleImage

class imageAdmin(admin.ModelAdmin):
    list_display = ["image_id", "image_url", "image_file", "date_created"]

admin.site.register(DalleImage, imageAdmin)