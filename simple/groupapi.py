from .models import GroupList, Create_item, Customer_create, Group_details
from .serializers import GroupNameSerializer, Item_create_serializer, custeomer_serializer, Group_DetailSerilizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

#group name create and show the assign value.
@api_view(['POST'])
def gruopname(request):
    data=GroupNameSerializer(data=request.data)
    if data.is_valid():
        data.save()
        # gs=GroupList(
        #     group_name=request.data.get('group_name')
        # )
        # if not gs.group_name:
        #     return Response('all feilds are required 123')
        # gs.save()
        return Response(data.data, status=status.HTTP_201_CREATED)
    return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

#create item in the group list using POST method
@api_view(['POST'])
def item_create(request):
    item=Item_create_serializer(data=request.data)
    if item.is_valid():
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)
    return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)

#create item in the GET method
@api_view(['GET'])
def item_item_get(request, pk):
    try:
        item=Create_item.objects.get(pk=pk)#model to call one by one data

    except item.DoesNotExist:
        return HttpResponse(status=404)
    data_serlizer=Item_create_serializer(item)#serilizer to call the module
    return Response(data_serlizer.data)

@api_view(['Delete'])
def item_delete(request, pk):
    try:
        item=Create_item.objects.get(pk=pk)
    except item.DoesNotExist:
        return HttpResponse(status=404)

    item.delete()
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def item_put(request, pk):
    try:
        item=Create_item.objects.get(pk=pk)
    except item.DoesNotExist:
        return HttpResponse(status=404)
    data_serilizer=Item_create_serializer(item, data=request.data)
    if data_serilizer.is_valid():
        data_serilizer.save()
        return Response(data_serilizer.data)
    return  Response(data_serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


#create customer  in the GET method
@api_view(['GET'])
def customer_list_get(request, pk):
    try:
        customer=Customer_create.objects.get(pk=pk)#model to call one by one data

    except customer.DoesNotExist:
        return HttpResponse(status=404)
    data_serlizer=Item_create_serializer(customer)#serilizer to call the module
    return Response(data_serlizer.data)

@api_view(['Delete'])
def customer_delete(request, pk):
    try:
        customer=Customer_create.objects.get(pk=pk)
    except customer.DoesNotExist:
        return HttpResponse(status=404)

    customer.delete()
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def customer_put(request, pk):
    try:
        customer=Customer_create.objects.get(pk=pk)
    except customer.DoesNotExist:
        return HttpResponse(status=404)
    data_serilizer=Item_create_serializer(customer, data=request.data)
    if data_serilizer.is_valid():
        data_serilizer.save()
        return Response(data_serilizer.data)
    return  Response(data_serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


#add group of customer and
#
@api_view(['POST'])
def group_add(request):
    #group_data = Group_details.objects.all()  # model to call one by one data
    item = Group_DetailSerilizer(data=request.data)
    if item.is_valid():
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)
    return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)

