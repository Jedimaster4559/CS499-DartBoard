# Generated by Django 3.1.5 on 2021-04-19 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_additional_player_statistics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='number_of_matches_list',
            new_name='number_of_matches_lost',
        ),
    ]