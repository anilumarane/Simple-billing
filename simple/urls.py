# posts/urls.py
from django.urls import path, re_path
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Polls API')
from . import views
#group craete in groupapi in data
from . import groupapi

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    re_path(r'swagger-docs/', schema_view),
    path('schema/', schema_view),
    #path('', views.home, name='home')
    path('signup', views.user_signup, name='signup'),
    path('customer', views.customer_list, name='customerlist'),
    path('reg/', views.user_register),
    #path('register', views.register),

    #create item list
    path('create_item', views.item_list),

    #group relateded url and
    path('group', groupapi.gruopname),# create a new group in method
    #This all feilds are related to the group item created
    path('item_create/', groupapi.item_create),#post  method for item_create in group
    path('item_get/<int:pk>', groupapi.item_item_get),#get method for items in group
    path('item_delete/<int:pk>', groupapi.item_delete),#delete method
    path('item_put/<int:pk>', groupapi.item_put), #put method

    # This all feilds are related to the group customer created on group
    path('customer_create/', groupapi.customer_list_get),  # post  method for item_create in group
    #path('item_get/<int:pk>', groupapi.item_item_get),  # get method for items in group
    path('customer_delete/<int:pk>', groupapi.customer_delete),  # delete method
    path('customer_put/<int:pk>', groupapi.customer_put),  # put method

    #group add method
    path('group_add', groupapi.group_add)
]
