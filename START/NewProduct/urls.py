from django.conf.urls import url

from . import views


app_name = 'NewProduct'

urlpatterns = [
    url(r'^create/$', views.product_create, name='product_create'),
]