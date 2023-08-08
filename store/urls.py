from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.cancel import Cancel
from .views.feedback import Feedback
from .middlewares.auth import  auth_middleware
from .views.view_order import View_Order






urlpatterns = [
   

    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'), 
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),

    path('view-order/<int:id>',View_Order.as_view(),name='view-order'),
    path('cancel/<int:id>',Cancel.as_view(),name='cancel'),
    path('feedback',Feedback.as_view(),name='feedback'),


    

]
