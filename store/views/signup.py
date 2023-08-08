from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        username=postData.get('username')
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        print(username)
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = []
        user=User(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        customer = Customer (user=user,
                            first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print (first_name,last_name, phone, email, password)
            customer.password = make_password (customer.password)
            user.password=customer.password
            user.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')


            my_customer_group[0].user_set.add(user)
            customer.register ()
            
            return redirect ('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = []
        if (not customer.first_name):
            error_message.append("Please Enter your First Name !!")
        elif len (customer.first_name) < 3:
            error_message.append( 'First Name must be 3 char long or more')
        elif not customer.last_name:
            error_message.append('Please Enter your Last Name')
        elif not customer.phone:
            error_message.append('Enter your Phone Number')
        elif len (customer.phone) < 10:
            error_message.append('Phone Number must be 10 char Long')
        elif len (customer.password) < 5:
            error_message.append('Password must be 5 char long')
        elif customer.isExists ():
            error_message.append('Email Address Already Registered ')
        
        
        if User.objects.filter(username=customer.user.username).exists():
            error_message.append(" username already exist")

            
        # saving

        return error_message
