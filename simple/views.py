from django.shortcuts import render
from .models import Customer_create, Create_item
from .serializers import  GroupNameSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
#from .forms import Create_itemForm

@api_view(['POST'])
def user_signup(request):
    user=UserReg(data=request.data)
    if user.is_valid():
        user.save()
        return Response(user.data, status=status.HTTP_201_CREATED)
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_register(request):
    form=UserProfileSerializer(data=request.data)
    if form.is_valid():
        form.save()
        return Response(form.data, status=status.HTTP_201_CREATED)
    return Response(form.errors,status=status.HTTP_400_BAD_REQUEST)



#customer create
@api_view(['GET', 'POST'])
def customer_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Customer_create.objects.all()
        serializer = Customer_create_serializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Customer_create_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# customer item create
@api_view(['POST'])
def item_list(request):
    form=Create_itemForm(request.data)
    if form.is_valid():
        form.save()

        item = Create_item(
            category_name=request.data.get('category_name'),
            item_name =request.data.get('item_name'),
            unit = request.data.get('unit'),
            quanity = request.data.get('quanity'),
            unit_quanity_type = request.data.get('unit_quinity_type'),
            unit_price = request.data.get('unit_price'),
            others = request.data.get('others'),
            service_charge = request.data.get('service_charge'),
            gst = request.data.get('gst'),
            total_amount = request.data.get('total_amount'),
            startdate = request.data.get('startdate'),
            enddate = request.data.get('enddate')
                )
        item.save()

        return Response(
                {'data':"201"}
            )

    else:
        return Response(data= {
               'error': str(form.errors.as_data())})

