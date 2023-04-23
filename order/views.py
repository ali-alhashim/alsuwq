from django.shortcuts import render

# Create your views here.

def your_orders(request):
    return render(request, 'order/your_orders.html',{})


def payselect(request):
    return render(request, 'order/payselect.html',{})
