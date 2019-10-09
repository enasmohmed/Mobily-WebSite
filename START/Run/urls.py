from django.conf.urls import url

from . import views

app_name = 'Run'

urlpatterns = [
    url(r'^list/$', views.product_list, name='product_list'),
    url(r'^(?P<main_category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^sub/(?P<sub_category_view>[-\w]+)/$', views.subcategory, name='subcategory'),
    url(r'^photo/(?P<product_slug>[-\w]+)/$', views.product_image, name='product_image'),
    url(r'^detail/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
