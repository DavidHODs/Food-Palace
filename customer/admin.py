from django.contrib import admin
from .models import OrderModel, MenuItem, Category

# Register your models here.

admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(OrderModel)