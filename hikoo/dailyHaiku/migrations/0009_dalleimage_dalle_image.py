# Generated by Django 4.1.5 on 2023-07-22 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyHaiku', '0008_dalleimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='dalleimage',
            name='dalle_image',
            field=models.ImageField(default='static/dailyHaiku/dalle/Background.png', max_length=1000, upload_to='static/dailyHaiku/dalle/'),
        ),
    ]
