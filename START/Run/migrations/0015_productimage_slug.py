# Generated by Django 2.2.5 on 2019-10-06 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Run', '0014_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='slug',
            field=models.SlugField(default=0, max_length=200),
        ),
    ]