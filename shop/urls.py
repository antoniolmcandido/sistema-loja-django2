from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("create_product/", views.product_create, name="product_create"),
    path("create_category/", views.category_create, name="category_create"),
    path("create_supplier/", views.supplier_create, name="supplier_create"),
    path("create_user/", views.user_create, name="user_create"),
]