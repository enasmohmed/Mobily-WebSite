# Generated by Django 2.2.5 on 2019-10-07 14:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewProduct', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newproduct',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
