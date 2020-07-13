from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
import bootstrapform


@login_required
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/index.html', context)


@login_required
def show(request, product_id):
    product = Product.objects.filter(pk=product_id)
    context = {'product': product[0] if len(product) > 0 else None}
    return render(request, 'products/show.html', context)


@login_required
def new(request):
    form = ProductForm(request.POST or None, request.FILES or None, None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products/form.html', {'form': form})


@login_required
def edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products/form.html', {'form': form})


@login_required
def delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    return render(request, 'products/confirm_delete.html', {'product': product})
