# Generated by Django 4.2.5 on 2024-02-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_duration',
            field=models.FloatField(),
        ),
    ]