from django.urls import path

from . import views

app_name = 'suppliers'

urlpatterns = [
    path('', views.SupplierView.as_view(), name='suppliers'),
    path('<int:id>', views.SingleSupplierView.as_view(), name='single_supplier'),
]
