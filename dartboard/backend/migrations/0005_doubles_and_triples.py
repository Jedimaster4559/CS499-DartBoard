# Generated by Django 3.1.5 on 2021-04-16 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_dartboardhit_is_foul'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchplayer',
            name='number_of_doubles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchplayer',
            name='number_of_triples',
            field=models.IntegerField(default=0),
        ),
    ]