from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

# Create your views here.
def product_list(request):
    produtos = Product.objects.all() # ORM
    paginator = Paginator(produtos, 3)

    page_number = request.GET.get('page')
    produtos = paginator.get_page(page_number)

    return render(request, 'product_list.html', {'produtos': produtos})