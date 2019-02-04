
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, m3_registered_mobile_number,
                    username,
                    email,
                    buisness_name,
                    aadhar_pan_number,
                    address,
                    pincode,
                    state,
                    password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not m3_registered_mobile_number:
            raise ValueError('Users must have an m3_registered_mobile_number address')

        user = self.model(
            m3_registered_mobile_number=m3_registered_mobile_number,
            username=username,
            email=self.normalize_email(email),
            buisness_name=buisness_name,
            aadhar_pan_number=aadhar_pan_number,
            address=address,
            pincode=pincode,
            state=state
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, m3_registered_mobile_number,
                    username,
                    email,
                    buisness_name,
                    aadhar_pan_number,
                    address,
                    pincode,
                    state,
                    password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            m3_registered_mobile_number,
            username,
            email,
            buisness_name,
            aadhar_pan_number,
            address,
            pincode,
            state,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

USERNAME_REGEX='^[0-9]*$'
class User(AbstractBaseUser):
    m3_registered_mobile_number = models.CharField(max_length=10,
                                                   validators=[RegexValidator(
                                                       regex=USERNAME_REGEX,
                                                       message='mobile number must be a contain numbers',
                                                       code='invalid mobile'
                                                   )],
                                                   unique=True)
    username = models.CharField(max_length=12)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    buisness_name=models.CharField(max_length=50)


    aadhar_pan_number=models.CharField(max_length=12, unique=True)
    # email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6,
                                        validators=[RegexValidator(
                                        regex=USERNAME_REGEX,
                                        message='mobile number must be a contain numbers',
                                        code='invalid mobile'
                                                   )])
    state_choices = (
    ("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"),
    ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ", "Jammu and Kashmir "),
    ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"), ("Odisha", "Odisha"), ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"),
    ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"),
    ("Lakshadweep", "Lakshadweep"), ("National Capital Territory of Delhi", "National Capital Territory of Delhi"),
    ("Puducherry", "Puducherry"))

    state = models.CharField(choices=state_choices, max_length=255, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'm3_registered_mobile_number'
    REQUIRED_FIELDS = [ 'username',
                        'email',
                        'buisness_name',
                        'aadhar_pan_number',
                        'address',
                        'pincode',
                        'state']

    def __str__(self):
        return self.m3_registered_mobile_number

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin