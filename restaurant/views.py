from django.shortcuts import render
from django.views import View
from django.utils.timezone import datetime
from customer.models import OrderModel, MenuItem
from .forms import MenuForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

# Create your views here.
class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
# class Dashboard(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        today = datetime.today()
        orders = OrderModel.objects.filter(
            created_on__year=today.year, created_on__month=today.month, created_on__day=today.day
            )
        
        unshipped_orders = []
        total_revenue = 0
        for order in orders:
            total_revenue += order.price

            if not order.is_shipped:
                unshipped_orders.append(order)

        context = {
            'orders':unshipped_orders,
            'total_revenue':total_revenue,
            'total_orders':len(orders)
        }
        return render(request, 'restaurant/dashboard.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()

class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, View):
# class OrderDetails(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        context = {
            'order':order,
        }

        return render(request, 'restaurant/order_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        order.is_shipped = True
        order.save()

        context = {
            'order':order
        }

        return render(request, 'restaurant/order_detail.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()


class CreateMenu(LoginRequiredMixin, UserPassesTestMixin, View):
# class CreateMenu(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()
        form =  MenuForm()
        context = {
            'menu_items':menu_items,
            'form':form,
        }
        return render(request, 'restaurant/create_menu.html', context)

    def post(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()
        form =  MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
        context = {
            'menu_items':menu_items,
            'form':form,
        }
        return render(request, 'restaurant/create_menu.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()