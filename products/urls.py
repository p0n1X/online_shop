from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductView.as_view(), name='product'),
    path('<int:id>', views.SingleProductView.as_view(), name='single_product'),
    path('category/<int:id>', views.ProductCategoryView.as_view(), name='product_category'),
]
