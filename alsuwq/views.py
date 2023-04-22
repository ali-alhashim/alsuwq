from django.shortcuts import render
from product.models import Product
from django.core.paginator import Paginator
from cart.models import Cart, CartItem
from cart.views import _cart_id

def home(request):
     try:
        
        cart      = None
        if request.user.is_authenticated:
            cartItems = CartItem.objects.filter(user = request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id = _cart_id(request))
            cartItems = CartItem.objects.filter(cart = cart, is_active=True)

        total = 0
        for item in cartItems:
            total += (item.product.price * item.quantity)
        tax = total * 15/100
        totalNoVAT = total - tax
     except Exception as e:
        cart      = None
        cartItems = None
        total     = 0
        tax       = 0
        totalNoVAT= 0

     top10Products = Product.objects.all().filter(is_available=True)[:10]
     products = Product.objects.all().filter(is_available=True)
     productsCount = products.count()

     page_number = request.GET.get('page')
     paginator = Paginator(products, 9) # show 9 product per page

    
     page_obj = paginator.get_page(page_number)
     return render(request, 'home/home.html', {"products":page_obj,"productsCount":productsCount,"cart":cart,"cartItems":cartItems,"total":total,"tax":tax,"totalNoVAT":totalNoVAT,"top10Products":top10Products})