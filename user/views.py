from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method =='POST':
       email    = request.POST.get('email')
       password = request.POST.get('password')
       user = auth.authenticate(email=email, password=password)

       if user is not None:
          #try:
              ## check if user add some items
              #cart = Cart.objects.get(cart_id=_cart_id(request))
              #is_cart_items_exists = CartItem.objects.filter(cart = cart).exists()
              #if is_cart_items_exists:
              #    cart_item = CartItem.objects.filter(cart=cart)
              #    for item in cart_item:
              #        item.user = user
              #        item.save()
                      
          #except Exception as e:
              #print(e)

          auth.login(request, user)  
          messages.success(request, 'Welcome '+str(user.name)) 
          return redirect('home')
       else:
           messages.error(request, 'invalid login !')
    return render(request, 'user/login.html',{})
