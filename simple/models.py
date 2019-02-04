from django.db import models
from datetime import date
# Create your models here.
import datetime
from django.contrib.auth.models import User

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.headline




# class UserRegister(models.Model):
#     buisness_name=models.CharField(max_length=50)
#     username=models.CharField(max_length=12, )
#     m3_registered_mobile_number=models.CharField(max_length=12,unique=True)
#     aadhar_pan_number=models.CharField(max_length=12, unique=True)
#     email=models.CharField(max_length=50)
#     address=models.CharField(max_length=50)
#     pincode=models.IntegerField()
#     state_choices = (
#     ("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"),
#     ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"),
#     ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ", "Jammu and Kashmir "),
#     ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"),
#     ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"),
#     ("Nagaland", "Nagaland"), ("Odisha", "Odisha"), ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"),
#     ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"),
#     ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"),
#     ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"),
#     ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"),
#     ("Lakshadweep", "Lakshadweep"), ("National Capital Territory of Delhi", "National Capital Territory of Delhi"),
#     ("Puducherry", "Puducherry"))
#
#     state = models.CharField(choices=state_choices, max_length=255, null=True, blank=True)
#     password=models.CharField(max_length=10)
#
#
# class Regsignup(models.Model):
#     #=models.CharField(max_length=50, unique=True)
#     buisness_name=models.CharField(max_length=50)
#     m3_number=models.CharField(max_length=12,unique=True)
#     aadhar_pan_number=models.CharField(max_length=12, unique=True)
#     address=models.CharField(max_length=50)
#     pincode=models.IntegerField()
#     # state_choices = (
#     # ("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"),
#     # ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"),
#     # ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ", "Jammu and Kashmir "),
#     # ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"),
#     # ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"),
#     # ("Nagaland", "Nagaland"), ("Odisha", "Odisha"), ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"),
#     # ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"),
#     # ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"),
#     # ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"),
#     # ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"),
#     # ("Lakshadweep", "Lakshadweep"), ("National Capital Territory of Delhi", "National Capital Territory of Delhi"),
#     # ("Puducherry", "Puducherry"))
#     # state = models.CharField(choices=state_choices, max_length=255, null=True, blank=True)
#     # {
#     #     "username": "ani11"
#     #                 "password": "anil1234",
#     #                             "profile": {
#     #     "buisness_name": "ms",
#     #     "m3_number": "123456789",
#     #     "aadhar_pan_number": "123456789",
#     #     "address": "bglr",
#     #     "pincode": "591244",
#     # }
#     # }


class Customer_create(models.Model):
    customer_name=models.CharField(max_length=250)
    mobile_number=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    house_number=models.CharField(max_length=250, blank=False)
    builiding_name=models.CharField(max_length=250)
    block_no=models.CharField(max_length=250)
    street=models.CharField(max_length=250)
    area=models.CharField(max_length=250)
    city=models.CharField(max_length=250, blank=False)
    pincode=models.CharField(max_length=250, blank=False)
    state=models.CharField(max_length=250, blank=False)
    country=models.CharField(max_length=30)
    def __str__(self):
        return self.customer_name

class Create_item(models.Model):
    category_name=models.CharField(max_length=250)
    item_name=models.CharField(max_length=250)
    unit_choices = (("CBM", "CUBIC METERS"), ("CCM ", "CUBIC CENTIMETERS "), ("CMS", "CENTIMETERS"),
                     ("GMS", "GRAMMES"), ("KGS ", "KILOGRAMMES "), ("KLR", "KILOLITRE"),("KME", "KILOMETER"),
                    ("MLT ", "MILILITRE "), ("MTR", "METERS"),("OTH ", "OTHERS "), ("QTL", "QUINTAL"),("SQF", "SQUARE FEET "),\
                    ("SQM", "SQUARE METERS"), ("TBS ", "TABLETS "), ("QTL", "QUINTAL"),
        )
    unit_name=models.CharField( choices=unit_choices, max_length=250)
    unit_quanity=models.IntegerField()
    unit_quanity_type_choices=(("BAG", "BAGS"), ("BOX ", "BOX "), ("BTL", "BOTTLES"),
                     ("DOZ", "DOZENS"), ("BDL ", "BUNDLES "), ("CAN", "CANS"),("PAC", "PACKETS"),
                    )
    unit_quanity_type=models.CharField(choices=unit_quanity_type_choices, max_length=250)
    unit_price=models.DecimalField(max_digits=5, decimal_places=3)
    others_charges=models.TextField(max_length=300)
    startdate = models.DateField(("Date"), default=datetime.date.today)
    enddate = models.DateField(blank=True, null=True)


#Group name craeted for user
class GroupList(models.Model):
    group_name=models.CharField(max_length=30)#unique=True
    # created_by = models.ForeignKey(User, related_name='grouplist', on_delete=models.CASCADE)
    # create_item=models.ForeignKey(Create_item,on_delete=models.CASCADE )
    # customer_create=models.ForeignKey(Customer_create, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name
#Group of foriegn key call to group and customer
class Group_details(models.Model):
    grouplist=models.ForeignKey(GroupList, related_name="grouplist", on_delete=models.CASCADE)
    customer_create=models.ManyToManyField(Customer_create, related_name='customer_create',)
