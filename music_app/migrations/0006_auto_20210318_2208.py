# Generated by Django 3.1.7 on 2021-03-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0005_auto_20210318_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='mood',
            field=models.IntegerField(choices=[(0.3, 'Turn Up'), ('0.5', 'Chill'), (0.8, 'Study')]),
        ),
    ]
