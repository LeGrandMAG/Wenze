# Generated by Django 3.0.14 on 2022-03-12 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magshop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='SLUG',
            new_name='slug',
        ),
    ]
