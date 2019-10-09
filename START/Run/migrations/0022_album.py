# Generated by Django 2.2.5 on 2019-10-06 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Run', '0021_remove_subcategory_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Run.Product')),
            ],
        ),
    ]
