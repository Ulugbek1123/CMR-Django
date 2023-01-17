from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('products/',views.products, name="products"),
    
    path('customers/<str:pk>/',views.customers, name="customer"),
    path('createOrder/<str:pk>/', views.createOrder, name="createOrder"),
    path('updateOrder/<str:pk>/', views.updateOrder, name="updateOrder"),
    path('deleteOrder/<str:pk>/', views.deleteOrder, name="deleteOrder"),
]
