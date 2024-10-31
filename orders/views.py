from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from .forms import *
from django.contrib import messages

# Create your views here.

def base_dashboard(request):
    return render(request, 'orders/base_dashboard.html')

def products_list(request):
    products = Products.objects.all()
    form = Add_ProductsForm()
    return render(request, 'orders/products.html', {'products': products, 'form': form} )

def add_product(request):
    if request.method == 'POST':
        form = Add_ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = Add_ProductsForm()
    products = Products.objects.all()
    return render(request, 'orders/products.html', {'products': products} )

def update_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        form = Add_ProductsForm(request.POST , instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = Add_ProductsForm(instance=product)
    return render(request, 'orders/products.html')

def delete_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
    return redirect('product_list')
