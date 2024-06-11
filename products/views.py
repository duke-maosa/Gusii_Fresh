from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Product, ProductImage
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()

    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    try:
        products_page = paginator.page(page_number)
    except PageNotAnInteger:
        products_page = paginator.page(1)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)

    return render(request, 'products/product_list.html', {'products': products_page})

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
            # Handle product images
            images = request.FILES.getlist('images')
            for image in images:
                ProductImage.objects.create(product=product, image=image)
            return redirect('products:product_detail', product_id=product.id)
    else:
        product_form = ProductForm()
    return render(request, 'products/create_product.html', {'product_form': product_form})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product = product_form.save()
            # Clear existing product images
            product.images.all().delete()
            # Handle updated product images
            images = request.FILES.getlist('images')
            for image in images:
                ProductImage.objects.create(product=product, image=image)
            return redirect('products:product_detail', product_id=product.id)
    else:
        product_form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'product': product, 'product_form': product_form})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products:product_list')
    return render(request, 'products/delete_product_confirm.html', {'product': product})
