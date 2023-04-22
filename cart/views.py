from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from product.models import Product
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
                                    cart_id=_cart_id(request)
                                  )
    cart.save()

    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product,user=request.user)
        else:
            cart_item = CartItem.objects.get(product=product,cart=cart)

        cart_item.quantity +=1 
        cart_item.save()
    except CartItem.DoesNotExist:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.create(
                                                product  = product,
                                                quantity = 1,
                                                cart     = cart,
                                                user     = request.user,
                                            )
        else:
             cart_item = CartItem.objects.create(
                                                product  = product,
                                                quantity = 1,
                                                cart     = cart,
                                                
                                            )

        cart_item.save()

    return redirect('cart')


def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product,id=product_id)

    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product=product, user=request.user)
    else:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        
    if cart_item.quantity > 1 :
       cart_item.quantity -=1
       cart_item.save()
    else:
       cart_item.delete()  
    return redirect('cart')

def delete_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product,id=product_id)

    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product = product, user=request.user) 
    else:
        cart_item = CartItem.objects.get(product = product, cart=cart) 

    cart_item.delete()  
    return redirect('cart')

def cart(request):
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

        
    return render(request,'cart/cart.html',{"cart":cart,"cartItems":cartItems,"total":total,"tax":tax,"totalNoVAT":totalNoVAT})



@login_required(login_url='login')
def checkout(request):
    try:
        
        cart      = None
        if request.user.is_authenticated:
            cartItems = CartItem.objects.filter(user = request.user.id, is_active=True)
        else:
            cart = Cart.objects.get(cart_id = _cart_id(request))
            cartItems = CartItem.objects.filter(cart = cart, is_active=True)


        total = 0
        for item in cartItems:
            total += (item.product.price * item.quantity)
        tax = total * 15/100
        totalNoVAT = total - tax
    except Exception as e:
        print(e)
        cart      = None
        cartItems = None
        total     = 0
        tax       = 0
        totalNoVAT= 0
    return render(request,'cart/checkout.html',{"cart":cart,"cartItems":cartItems,"total":total,"tax":tax,"totalNoVAT":totalNoVAT})


