from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from NewProduct.forms import ProductCreateForm


def product_create(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            # new_form.user = request.user
            new_form.save()
            messages.success(request, 'Product Model Created Successfully')
            return redirect('/')

    else:
        form = ProductCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)