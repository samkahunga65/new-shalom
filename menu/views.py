from django.shortcuts import render

def index(request):
    return render(request, 'menu/index.html')

def order(request):
    return render(request, 'menu/order.html')

def menu(request):
    return render(request, 'menu/menu.html')

# def store(request):
#     return render(request, 'menu/index.html')

