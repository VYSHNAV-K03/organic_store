from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order,Orderbase
from .models.feedback import Feedback
from django.contrib.auth.models import Group

admin.site.unregister(Group)
# class OrderInline(admin.TabularInline):
#     model = Order
#     extra = 1

# class OrderbaseAdmin(admin.ModelAdmin):
#     inlines = [OrderInline]

# admin.site.register(Orderbase, OrderbaseAdmin)

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'orderbase', 'product', 'customer', 'quantity', 'price')

#     list_filter = ('orderbase',)
    


# admin.site.register(Order, OrderAdmin)

class OrderInline(admin.TabularInline):
    model = Order
    extra = 0
    max_num = 0

    readonly_fields = ['get_name','product', 'customer', 'quantity', 'price'  ]
    can_delete = False

class OrderbaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_order_number', 'customer', 'date', 'status', 'total')
    inlines = [OrderInline]

    def get_order_number(self, obj):
        return obj.order_set.first().id
    get_order_number.short_description = 'Order Number'

admin.site.register(Orderbase, OrderbaseAdmin)



class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category','quantity']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']




# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Feedback)
admin.site.register(Category)
admin.site.register(Customer)
# admin.site.register(Order)
# admin.site.register(Orderbase,OrderbaseAdmin)