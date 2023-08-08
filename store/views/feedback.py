from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from store.models.orders import Orderbase
from store.models.feedback import Feedback as FMODEL

class Feedback(View):
    def post(self,request):
        customer = request.session.get('customer')
        order_id=request.POST['order_id']
        feedbackmsg=request.POST['feedback']
        order=Orderbase.objects.get(id=order_id)
        feedback=FMODEL.objects.filter(order=order).first()
        feedback.feedbackmsg=feedbackmsg
        feedback.save()
        messages.info(request,"feedback submitted")
        return HttpResponseRedirect(f'view-order/{order_id}')



