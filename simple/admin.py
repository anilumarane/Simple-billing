from django.contrib import admin
from .models import Create_item, Customer_create, GroupList,Group_details
# Register your models here.
admin.site.register(Create_item)


class Customer_createAdmin(admin.ModelAdmin):
 list_display = ['id', 'customer_name', 'mobile_number', 'email',
 'house_number', 'builiding_name', 'block_no', 'street',
 'area', 'city', 'pincode', 'state', 'country']
 list_filter = ['customer_name', 'mobile_number', 'pincode']
 #inlines = [OrderItemInline]
#
# admin.site.register(Order, OrderAdmin)
admin.site.register(Customer_create, Customer_createAdmin)
admin.site.register(GroupList)
admin.site.register(Group_details)