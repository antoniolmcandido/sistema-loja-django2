from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product, Category, Supplier
from .forms import ProductForm, CategoryForm, SupplierForm, UserForm

def user_create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Não salva ainda no banco
            user.set_password(form.cleaned_data["password"])  # Faz o hash da senha
            user.save()  # Agora salva com a senha hashada
            return redirect("product_list")
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})

# Create your views here.
def product_list(request):
    produtos = Product.objects.all() # ORM
    paginator = Paginator(produtos, 3)

    page_number = request.GET.get('page')
    produtos = paginator.get_page(page_number)

    return render(request, 'product_list.html', {'produtos': produtos})

def product_create(request):
    if request.method == 'POST':
        # Se o método for POST, o formulário foi enviado
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo produto no banco de dados
            return redirect('product_list')  # Redireciona para a lista de produtos
    else:
        # Se o método for GET, exibe um formulário em branco
        form = ProductForm()

    # Renderiza o template do formulário, passando o form como contexto
    return render(request, 'product_form.html', {'form': form})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_create')
    else:
        form = CategoryForm()

    return render(request, 'category_form.html', {'form': form})

def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_create')
    else:
        form = SupplierForm()

    return render(request, 'supplier_form.html', {'form': form})