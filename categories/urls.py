from django.urls import path

from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.CategoryView.as_view(), name='categories'),
    path('<int:id>', views.SingleCategoryView.as_view(), name='single_category'),
]
