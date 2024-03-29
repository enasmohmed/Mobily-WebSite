# Generated by Django 2.2.5 on 2019-10-05 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Run', '0002_auto_20191005_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name=' My Gallery')),
                ('category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='Run.Product')),
            ],
        ),
    ]
