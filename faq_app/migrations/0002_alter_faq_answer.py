# Generated by Django 5.1.5 on 2025-02-02 05:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
