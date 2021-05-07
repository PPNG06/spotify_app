# Generated by Django 3.1.7 on 2021-03-15 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_auto_20210309_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='style',
            field=models.CharField(choices=[('RAP', 'Rap'), ('LOFI', 'Lofi'), ('POP', 'Pop'), ('ELECTRO', 'Electro'), ('ROCK', 'Rock'), ('JAZZ', 'Jazz')], default='Rap', max_length=100),
        ),
    ]