from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer_create,  Create_item, GroupList,Group_details
from django.core.exceptions import ValidationError

from rest_framework.response import Response

# class UserReg(serializers.ModelSerializer):
#     #snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#     class Meta:
#         model = UserRegister
#         fields = '__all__'
#         extra_kwargs = {'password':{'write_only':True}}
#
#
#     def create(self, validated_data):
#         user=UserRegister(
#         buisness_name=validated_data['buisness_name'],
#         username = validated_data['username'],
#         m3_registered_mobile_number = validated_data['m3_registered_mobile_number'],
#         aadhar_pan_number =validated_data['aadhar_pan_number'],
#         email =validated_data['email'],
#         address = validated_data['address'],
#         pincode = validated_data['pincode'],
#
#         )
#         return user

# class ProfileSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model=Regsignup
#         fields=['buisness_name',
#                 'm3_number',
#                 'aadhar_pan_number',
#                 'address',
#                 'pincode']


# class UserProfileSerializer(serializers.ModelSerializer):
#     profile=ProfileSerilizer(many=True)
#
#     class Meta:
#         model=User
#         fields=('username',
#                 'email',
#                 'password',
#                 'profile')
#         extra_kwargs={'password':{'write_only':True}
#                       }
#     # def create(self, validated_data):
#     #     prof=validated_data.pop('profile')
#     #     user=User.objects.create(**prof)
#     #     profile_data=Regsignup.objects.create(user=user, **validated_data)
#     #     return profile_data
#     def create(self, validated_data):
#         profile_data=validated_data.pop('profile')
#         password=validated_data.pop('password')
#         user=User(**validated_data)
#         #user.set_password(validated_data['password'])
#         user.set_password(password)
#         user.save()
#         a=Regsignup.objects.create(user=user, **profile_data)
#         for i in a:
#             return i
#     """ def create(self, validated_data):
#         profile_data=validated_data.pop('profile')
#         #a = Regsignup.objects.create(**profile_data)
#         #user=User.objects.create(**validated_data, profile=a)
#         #return user
#
#         user = User(
#             username=validated_data['username'],
#             email=validated_data['email']
#          )
#         user.set_password(validated_data['password'])
#         user.save()
#         a=Regsignup.objects.create(**profile_data)
#         return user, a
#
# """
#


#create group name for each group
class GroupNameSerializer(serializers.ModelSerializer):
    #group_name=serializers.CharField(max_length=50)
    class Meta:
        model=GroupList
        fields=['group_name']

    # extra_kwargs = {
    #     'group_name': {
    #         'write_only': True  # Function-based validator
    #     }
    # }

    def validate(self, data):
        group_name=data['group_name']
        group_query=GroupList.objects.filter(group_name=group_name)
        if group_query.exists():
            raise serializers.ValidationError('this user group alraedy exists')
        return data


    def validate_group_name(self, value):
        data=self.get_initial()
        #group2=data.get('group2')
        group_name=value
        if group_name=='anil':
            raise serializers.ValidationError(' group name is required not blank')
        return value

    def create(self, validated_data):
        group_name=validated_data['group_name']
        group_id=GroupList(
            group_name=group_name
        )
        group_id.save()
        return validated_data

#group customer_item create api needed
class Item_create_serializer(serializers.ModelSerializer):
    class Meta:
        model=Create_item
        fields=[
            'category_name',
            'item_name',
            'unit_name',
            'unit_quanity',
            'unit_quanity_type',
            'unit_price',
            'others_charges',
            'startdate',
            'enddate'
        ]


#custer to create in group of system
class custeomer_serializer(serializers.ModelSerializer):
    class Meta:
        model=Customer_create
        fields='__all__'



#add to group in the list
class Group_DetailSerilizer(serializers.ModelSerializer):

    class Meta:
        model=Group_details
        fields='__all__'


    def validate(self, attrs):
        pass

    