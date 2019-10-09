from django.db import models
from django.urls import reverse



class MainCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Run:product_list_by_category', args=[self.slug])

class SubCategory(models.Model):
    category = models.ForeignKey(MainCategory, related_name='subcategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Run:subcategory', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(SubCategory,related_name='product', on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, default=0,  unique=True)
    Image = models.ImageField(null=True, blank=True, upload_to='media/images/', default='media/images/default.png')
    description = models.TextField(blank=True)
    model_number = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Run:product_detail', args=[self.slug])



