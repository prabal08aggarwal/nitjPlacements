# Generated by Django 3.1.5 on 2021-05-15 15:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewExperience', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewexp',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
