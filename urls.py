from django.urls import path
from .views import product_list, ProductAPIView

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product_detail'),
]