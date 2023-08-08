
from django.shortcuts import render, redirect
from django.views import View
from store.models.orders import Order,Orderbase
from store.models.feedback import Feedback

class View_Order(View):
    def get(self,request,id):
        customer = request.session.get('customer')
        orderbase=Orderbase.objects.get(id=id)
        orders=Order.objects.filter(customer=customer,orderbase=orderbase)
        feedback=Feedback.objects.filter(order=orderbase).first()
        return render(request,'view-order.html',{'orders':orders,'orderbase':orderbase,'feedback':feedback})
