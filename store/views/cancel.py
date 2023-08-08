from django.views import View
from store.models.orders import Order,Orderbase
from django.contrib import messages
from django.shortcuts import render, redirect
from store.models.product import Products

class Cancel(View):
    def get(self,request,id):
        customer = request.session.get('customer')
        order=Order.objects.filter(customer=customer,orderbase_id=id)
        for i in order:
            product_id=i.product_id
            qty=i.quantity
            product=Products.objects.get(id=product_id)
            product.quantity+=qty
            product.save()
        Order.objects.filter(customer=customer,orderbase_id=id).delete()
        Orderbase.objects.get(id=id).delete()
        messages.info(request,"Order cancelled sucessfully")
        return redirect('orders')

