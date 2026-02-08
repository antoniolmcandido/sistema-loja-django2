from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from shop.models import Category, Supplier, Product
from .serializers import CategorySerializer, SupplierSerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Configuração dos Filtros
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Campos filtrados
    filterset_fields = ['category', 'supplier']

    # Campos pesquisados
    search_fields = ['name', 'description']

    # Campos para ordenação
    ordering_fields = ['price', 'name', 'stock']

