# Generated by Django 2.2.5 on 2019-10-06 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Run', '0026_auto_20191006_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Run.Product')),
            ],
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
