from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

@login_required
def home(request):
    products = Product.objects.all()
    return render(request, 'home/home.html', {'products': products})

def home_view(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request, 'home.html', {'products': products, 'query': query})



def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'home/product_detail.html', {'product': product})



def home(request):
    query = request.GET.get('q')  # get the search text
    if query:
        products = Product.objects.filter(name__icontains=query)  # search by name
    else:
        products = Product.objects.all()
    
    return render(request, 'home/home.html', {'products': products, 'query': query})

def payment_page(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    if request.method == "POST":
        # Simulate payment success
        return redirect('payment_success')
    
    return render(request, 'home/payment.html', {'product': product})

def payment_success(request):
    return render(request, 'home/payment_success.html')