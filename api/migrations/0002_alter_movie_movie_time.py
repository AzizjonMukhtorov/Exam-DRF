# Generated by Django 5.0.3 on 2024-03-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_time',
            field=models.TimeField(),
        ),
    ]
