# Generated by Django 3.1.5 on 2021-04-20 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_match_last_win'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='last_win',
            new_name='match_date',
        ),
    ]