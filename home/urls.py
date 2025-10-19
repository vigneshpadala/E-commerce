from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment/<slug:slug>/', views.payment_page, name='payment_page'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    
]

    