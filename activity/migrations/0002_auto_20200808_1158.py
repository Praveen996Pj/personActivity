# Generated by Django 3.0.7 on 2020-08-08 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personactivity',
            old_name='state_time',
            new_name='start_time',
        ),
    ]
