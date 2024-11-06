from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from .forms import *
from django.contrib import messages
import pandas as pd

# Create your views here.

def base_dashboard(request):
    return render(request, 'orders/base_dashboard.html')

def products_list(request):
    products = Products.objects.all()
    form = Add_ProductsForm()
    return render(request, 'orders/products.html', {'products': products, 'form': form} )

def add_product(request):
    if request.method == 'POST':
        form = Add_ProductsForm(request.POST, request.FILES)
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


def product_view(request):
    products = Products.objects.all()
    form = Add_ProductsForm()
    return render(request, 'orders/product_view.html', {'products': products, 'form': form})

def categories_list(request):
    return render(request, 'orders/categories.html')

def file_upload(request):
    if request.method == 'POST':
        form = CSV_fileUpload(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            try:
                data = pd.read_csv(csv_file)
                for _, row in data.iterrows():
                    # Check for missing required fields (e.g., 'code', 'name') before processing
                    if pd.isna(row['code']) or pd.isna(row['name']):
                        continue  # Skip rows with missing 'code' or 'name'

                    # Ensure proper handling of any missing or NaN values in other columns
                    product_data = {
                        'code': row.get('code', ''),
                        'name': row.get('name', ''),
                        'description': row.get('description', ''),
                        'type': row.get('type', ''),
                        'brand': row.get('brand', ''),
                        'category': row.get('category', ''),
                        'price': row.get('price', 0),  # Default to 0 if price is missing
                        'stock': row.get('stock', 0),  # Default to 0 if stock is missing
                        'product_color': row.get('product_color', ''),
                        'image': row.get('image', ''),
                    }

                    # Check if price and stock are numeric
                    if not isinstance(product_data['price'], (int, float)) or not isinstance(product_data['stock'], (int, float)):
                        continue  # Skip rows with invalid price or stock values

                    # Try to get or create product
                    product = Products.objects.filter(code=row['code']).first()
                    
                    if product:
                        # Update product if it exists
                        product.name = row['name']
                        product.description = row['description']
                        product.type = row['type']
                        product.brand = row['brand']
                        product.category = row['category']
                        product.price = row['price']
                        product.stock = row['stock']
                        product.product_color = row['product_color']
                        product.image = row['image']
                        product.save()
                    else:
                        # Create new product if it doesn't exist
                        Products.objects.create(**product_data)

                messages.success(request, 'Products uploaded successfully')
                return redirect('product_list')
            except Exception as e:
                messages.error(request, f'Error processing file{e}')
    else:
        form = CSV_fileUpload()                
            
    return render(request, 'orders/file_upload.html',{'form': form})