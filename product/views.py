from django.shortcuts import render, get_object_or_404, HttpResponse
from category.models import Category
from .models import Product
from django.core.paginator import Paginator
from cart.models import CartItem
from cart.views import _cart_id
# Create your views here.


def store(request, category_slug=None):
    categories = None
    products   = None

    
    if category_slug != None:
        categories = get_object_or_404(Category, slug = category_slug)
        products   = Product.objects.filter(category = categories, is_available=True)
        productsCount = products.count()
    else:   
        products = Product.objects.all().filter(is_available=True)
        productsCount = products.count()

    page_number = request.GET.get('page')
    paginator = Paginator(products, 9) # show 9 product per page

    
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/home.html',{"products":page_obj,"productsCount":productsCount})


def product_detail(request,category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
        in_cart        = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    
    return render(request,'home/product_detail.html',{"product":single_product,"in_cart":in_cart})
