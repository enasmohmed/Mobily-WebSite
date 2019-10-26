from django.shortcuts import render, get_object_or_404, render_to_response
from django.views import View

from Run.models import MainCategory, Product, SubCategory


def HomePageView(request, category_slug=None):
    category = None
    categories = MainCategory.objects.all()
    if category_slug:
        category = get_object_or_404(MainCategory, slug=category_slug)

    context = {
        'category': category,
        'categories': categories
    }
    return render(request, 'index.html', context)


def product_list(request, main_category_slug=None):
    category = None
    categories = MainCategory.objects.all()
    products = Product.objects.filter(available=True)
    if main_category_slug:
        sub_category = get_object_or_404(MainCategory, slug=main_category_slug)
        products = products.filter(category=category)

    context = {
        'sub_category': sub_category,
        'categories': categories,
        'products': products
    }
    return render(request, 'list.html', context)



def subcategory(request, sub_category_view):
    category = MainCategory.objects.get(slug=sub_category_view)
    subcategories = SubCategory.objects.filter(category=category)
    return render(request, 'sub.html',
                  {'subcategories': subcategories})



def product_image(request, product_slug):
    category = SubCategory.objects.get(slug=product_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'photo.html',
                  {'products': products})



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'detail.html',
                  {'product': product})



def ContactUs(request):
    return render(request, 'contact_us.html')


