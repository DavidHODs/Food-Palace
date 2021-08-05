from django.urls import path
from .views import Dashboard, OrderDetails, CreateMenu


app_name = 'restaurant'

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('orders/<int:pk>/', OrderDetails.as_view(), name='order-details'),
    path('create-menu/', CreateMenu.as_view(), name='create-menu'),
]