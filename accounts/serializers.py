from rest_framework import serializers
from .models import User
from django.db.models import Q
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import exceptions
from django.contrib.auth import authenticate

#login serializer based on the class api
class LoginViewSerilizer(serializers.Serializer):
    m3_registered_mobile_number=serializers.CharField()
    password=serializers.CharField()

    #now validation data
    def validate(self, data):
        m3_registered_mobile_number=data.get('m3_registered_mobile_number', '')
        password = data.get('password', '')
        if not m3_registered_mobile_number :
            raise exceptions.ValidationError('please enter m3_registered_mobile_number')
        if not password:
            raise exceptions.ValidationError(' please enter correct password')
        if m3_registered_mobile_number and password:
            user = authenticate(m3_registered_mobile_number=m3_registered_mobile_number, password=password)
            if user:
                if user.is_active:
                    data['user']=user
                else:
                    msg='User is deactivate.'
                    raise exceptions.ValidationError(msg)
            else:
                msg='Unble to login with given credentials.'
                raise exceptions.ValidationError(msg)
        else:
            msg='must provide username and password'
            raise exceptions.ValidationError(msg)
        return data
#user serializer
class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields =('m3_registered_mobile_number','buisness_name','username','aadhar_pan_number','email','address','pincode','state','password')

    def validate(self, data):
        m3_registered_mobile_number = data['m3_registered_mobile_number']
        aadhar_pan_number = data['aadhar_pan_number']
        state=data['state']
        user_query=User.objects.filter(m3_registered_mobile_number=m3_registered_mobile_number)
        if  user_query.exists():
            raise serializers.ValidationError(' m3 user regester already register')
        user_query1=User.objects.filter(aadhar_pan_number=aadhar_pan_number)
        if user_query1.exists():

            raise serializers.ValidationError('aadhar number or pan number alrady regester')

        if not m3_registered_mobile_number:
            raise serializers.ValidationError('enter mobile number')
        if not aadhar_pan_number:
            raise serializers.ValidationError('enter valid number')

        if len(m3_registered_mobile_number)<11:
            raise serializers.ValidationError('enter valid m3_number')
        if len(aadhar_pan_number)<13:
            raise serializers.ValidationError(' enter valid aadhar number')

        return data



# class UserLoginSerilizer(serializers.ModelSerializer):
#     #token = serializers.CharField(allow_blank=True, read_only = True)
#     class Meta:
#         model=User
#         fields=(
#             'm3_registered_mobile_number',
#             'password',
#         )
#         extra_kwargs = {"password":
#                             {"write_only":True }}
#     def validate(self, data):
#         user_obj=None
#         m3_registered_mobile_number=data.get("m3_registered_mobile_number")
#         password=data['password']
#         if not m3_registered_mobile_number and not password:
#             raise serializers.ValidationError('m3_registered_mobile number required')
#
#         user=User.objects.filter(
#             Q(m3_registered_mobile_number=m3_registered_mobile_number)
#         ).distinct()
#         if user.exists() and user.count() == 1:
#             user_obj=user.first()
#         else:
#             raise serializers.ValidationError('m3_registered_mobile_number number is invalid')
#         if user_obj:
#             if not user_obj.check_password(password):
#                 raise serializers.ValidationError('Incorrect credentials please try again.')
#         #data["token"] = "SOME RANDOM TOKEN"
#         return data
#
#     # def create(self, validated_data):
#     #     user = User(
#     #         m3_registered_mobile_number=validated_data['m3_registered_mobile_number']
#     #
#     #     )
#     #     user.set_password(validated_data['password'])
#     #     user.save()
#     #     #Token.objects.create(user=user)
#     #     return user
#
#
# class UserLoginSerilizer123(serializers.ModelSerializer):
#     token = serializers.CharField(allow_blank=True, read_only = True)
#     class Meta:
#         model=User
#         fields=[
#             'm3_registered_mobile_number',
#             'password',
#             'token',
#         ]
#         extra_kwargs = {"password":
#                             {"write_only": True}}
#
