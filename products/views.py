from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, ProductImage
from .forms import ProductForm

@login_required
def product_list(request):
    products = Product.objects.all()
    # Add pagination logic here if needed
    return render(request, 'products/product_list.html', {'products': products})

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
def create_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.seller = request.user
            product.save()
            for image in request.FILES.getlist('images'):
                ProductImage.objects.create(product=product, image=image)
            messages.success(request, 'Product created successfully.')
            return redirect('products:product_detail', product_id=product.id)
        else:
            messages.error(request, 'Error creating product. Please check the form.')
    else:
        product_form = ProductForm()
    return render(request, 'products/create_product.html', {'product_form': product_form})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.seller = request.user
            product.save()
            product.images.all().delete()
            for image in request.FILES.getlist('images'):
                ProductImage.objects.create(product=product, image=image)
            messages.success(request, 'Product updated successfully.')
            return redirect('products:product_detail', product_id=product.id)
        else:
            messages.error(request, 'Error updating product. Please check the form.')
    else:
        product_form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'product': product, 'product_form': product_form})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('products:product_list')
    return render(request, 'products/delete_product_confirm.html', {'product': product})
