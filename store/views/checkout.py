from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.feedback import Feedback

from store.models.product import Products
from store.models.orders import Order,Orderbase

class CheckOut(View):
    def post(self, request):
       
        house = request.POST.get('house')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        
        # print(Order.objects.filter(customer_id=customer).last().order_no)
        # Manual update of order number
        # if(Order.objects.filter(customer_id=customer).exists()):
        #     last=Order.objects.filter(customer_id=customer).last().order_no
        #     print("object already exist",last)
        #     order_no=last+1
        # else:
        #     order_no=1
        #     print("object initialized")
        # print(order_no)
        total=0
        for i in products:
            total=total +i.price*cart.get(str(i.id))
        print(total)
        # print( phone, customer, cart, products)

        n=Orderbase.objects.create(customer=Customer(id=customer),
                          phone=phone,
                          house=house,
                          street=street,
                          city=city,
                          state=state,
                          total=total)
        feedback=Feedback.objects.create(order=n)
        order_no=n.pk
        for product in products:
            max_qty=product.quantity
            order_qty=cart.get(str(product.id))
            print("qty is",order_qty,"max qty is",max_qty)
            order = Order(customer=Customer(id=customer),
                          orderbase=Orderbase(id=order_no),
                          product=product,
                          price=product.price,
                          quantity=order_qty)
                          
            order.save()
            max_qty=max_qty-order_qty
            if(max_qty<0):
                max_qty=0
            print("new max qty",max_qty)
            product.quantity=max_qty
            product.save()
        
        
        request.session['cart'] = {}

        return redirect('cart')
