from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from .forms import RegistrationForm
from . models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

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



@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Good bye!') 
    return redirect('home') 



###############################

def register(request):
    if request.method == 'POST':
       form = RegistrationForm(request.POST)
       if form.is_valid():
           name    = form.cleaned_data['name']  
           mobile  = form.cleaned_data['mobile']
           email   = form.cleaned_data['email']
           address = form.cleaned_data['address']
           password= form.cleaned_data['password']
           user = User.objects.create(
                                       name     = name,
                                       mobile   = mobile,
                                       email    = email,
                                       address  = address, 
                                      
                                     )
           user.set_password(password)
           user.save()

           # user Activation
           current_site = get_current_site(request)
           mail_subject = 'please activate your account'
           message      = render_to_string('user/account_verification_email.html',{"user"  :user,
                                                                                    "domain":current_site,
                                                                                    "uid"   :urlsafe_base64_encode(force_bytes(user.pk)),
                                                                                    "token" : default_token_generator.make_token(user),
                                                                                    })
           to_email = email
           send_email = EmailMessage(mail_subject, message, to=[to_email])
           send_email.send()
           messages.success(request, 'Registration successful, activation link has been sent to your email')
           return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html',{"form":form})

##############################################



def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        pass
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your Account is activated Thank you.')
    else:
        messages.error(request, 'invlied activation link!') 
    return redirect('login')



###################################################

@login_required(login_url='login')
def dashboard(request):
    
    return render(request, 'user/dashboard.html',{})





#####################################

def forgotPassword(request):
    if request.method =='POST':
        email = request.POST.get('email')
       
        if   User.objects.filter(email__iexact=email).exists():

            user = User.objects.get(email__iexact=email)
            current_site = get_current_site(request)
            mail_subject = 'Reset Password'
            message      = render_to_string('user/forgotPassword_email.html',{"user"  :user,
                                                                                        "domain":current_site,
                                                                                        "uid"   :urlsafe_base64_encode(force_bytes(user.pk)),
                                                                                        "token" : default_token_generator.make_token(user),
                                                                                        })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'Reset Password link sent to your email')
        else:
            messages.error(request, 'the Email Does Not Exist!')

    return render(request, 'user/forgotPassword.html',{})




###############################################################

def resetPassword(request, uidb64, token):
    current_site = get_current_site(request)
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        messages.error(request, 'invlied  User') 
        return redirect('forgotPassword')


    if user is not None and default_token_generator.check_token(user, token):
        ## set new password
        if request.method =='POST':
            if request.POST.get('password') == request.POST.get('confirm_password'):
                user.set_password(request.POST.get('password'))
                user.save()
                messages.success(request, 'Your password has been reset Thank you.')
                return redirect('login')
        else:
               return render(request, 'user/resetPassword.html',{"user":user, "uid":uidb64,"token":token,"domain":current_site})    
        
    else:
        messages.error(request, 'invlied  link!') 
        return redirect('forgotPassword')
    



def your_addresses(request):
    return render(request, 'user/your_addresses.html',{})
