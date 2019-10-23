from django.db import models

# Create your models here.
from django.utils import timezone
from ckeditor.fields import RichTextField




class NewProduct(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, default=0,  unique=True)
    Image = models.ImageField(null=True, blank=True, upload_to='media/')
    description = RichTextField()
    model_number = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
