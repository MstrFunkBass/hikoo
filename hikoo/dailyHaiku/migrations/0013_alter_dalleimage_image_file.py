# Generated by Django 4.1.5 on 2023-07-22 19:48

from django.db import migrations, models
import hikoo.custom_azure


class Migration(migrations.Migration):

    dependencies = [
        ('dailyHaiku', '0012_alter_dalleimage_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dalleimage',
            name='image_file',
            field=models.ImageField(default='background/none-image.png', max_length=1000, storage=hikoo.custom_azure.AzureMediaStorage, upload_to='background/'),
        ),
    ]