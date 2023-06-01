from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.OrderView.as_view(), name='orders'),
    path('<int:id>', views.SingleOrderView.as_view(), name='single_order'),
]
