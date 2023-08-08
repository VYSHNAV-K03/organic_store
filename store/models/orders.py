from django.db import models
from .product import Products
from .customer import Customer
import datetime


class Orderbase(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    house=models.CharField(max_length=50,default='',null=True)
    street=models.CharField(max_length=50,default='',null=True)
    city=models.CharField(max_length=50,default='',null=True)
    state=models.CharField(max_length=50,default='',null=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)
    total=models.IntegerField()



    
    def get_addr(self):
        return f'{self.house},{self.street},{self.city},{self.state}'
    
    def address(self):
        return f'{self.house},{self.street},{self.city},{self.state}'

class Order(models.Model):
    orderbase=models.ForeignKey(Orderbase,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()

    def get_name(self):
        return self.product.name
    
    


   
    
  

    def placeOrder(self):
        self.save()

    def get_address(self):
        return f'{self.house},{self.street},{self.city},{self.state}'    
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')


