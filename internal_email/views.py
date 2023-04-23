from django.shortcuts import render

# Create your views here.

def your_email(request):
    return render(request, 'internal_email/your_email.html',{})
