from django import forms
#from .models import Regsignup
import datetime

# class Create_itemForm(forms.Form):
#     category_name=forms.CharField(max_length=250)
#     item_name=forms.CharField(max_length=250)
#     unit=forms.CharField(max_length=250)
#     quanity=forms.IntegerField()
#     unit_quanity_type=forms.CharField(max_length=250)
#     unit_price=forms.DecimalField(max_digits=5, decimal_places=3)
#     others=forms.CharField(max_length=300, widget=forms.Textarea)
#     service_charge=forms.DecimalField(max_digits=5, decimal_places=2)
#     gst=forms.DecimalField(max_digits=5, decimal_places=2)
#     total_amount=forms.DecimalField(max_digits=10, decimal_places=2)
#     startdate = forms.DateField()
#     enddate = forms.DateField()
#
#     class Meta:
#         model=Regsignup
#         fields={'category_name','item_name','unit','quanity','unit_quanity_type','unit_price','others',
#                 'service_charge','gst', 'total_amount','startdate','startdate'}