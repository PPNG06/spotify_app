# Generated by Django 3.1.7 on 2021-03-15 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='title',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
