from django.contrib import admin

# Register your models here.
from Run.models import Product, SubCategory, MainCategory

admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Product)
# admin.site.register(ProductPhoto)


