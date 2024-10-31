from django.urls import path
from . import views

urlpatterns = [
    path('',views.base_dashboard,name='base'),
    path('products/',views.products_list,name='product_list'),
    path('add_product/',views.add_product,name='add_product'),
    path('update_product/<int:pk>/',views.update_product,name='update_product'),
    path('delete_product/<int:pk>/',views.delete_product,name='delete_product')
]
