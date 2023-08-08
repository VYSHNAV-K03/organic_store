from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order,Orderbase
from store.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        # orders = Order.get_orders_by_customer(customer)
        # next url
        orders=Orderbase.objects.filter(customer=customer)
        # orders=[]
        #  for i in orders_no:
        #      order_details=Order.objects.filter(customer=customer,order_no=i)
        #      orders.append(order_details)
            
        print(orders)
        return render(request,'orders.html',{'orders':orders})
