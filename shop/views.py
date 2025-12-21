from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    produtos = Product.objects.all() # ORM
    return render(request, 'product_list.html', {'produtos': produtos})


