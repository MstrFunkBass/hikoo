# Generated by Django 4.1.5 on 2023-07-22 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailyHaiku', '0006_alter_image_image_file_alter_image_image_url'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='DalleImage',
        ),
    ]
