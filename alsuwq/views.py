from django.shortcuts import render
from product.models import Product
from django.core.paginator import Paginator


def home(request):
     products = Product.objects.all().filter(is_available=True)
     productsCount = products.count()

     page_number = request.GET.get('page')
     paginator = Paginator(products, 9) # show 9 product per page

    
     page_obj = paginator.get_page(page_number)
     return render(request, 'home/home.html', {"products":page_obj,"productsCount":productsCount})