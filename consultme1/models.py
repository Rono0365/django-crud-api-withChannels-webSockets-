from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#Clientfrom django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Lawyer(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='lawyer_images', null=True)
    company = models.CharField(max_length=100, default='')
    short_description = models.CharField(max_length=100, default='')
    long_description = models.CharField(max_length=10000, default='')
    quote_range = models.CharField(max_length=100, default='')
    license_number = models.CharField(max_length=100, default='')


class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=10000, default='')


class LawFirm(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=10000, default='')


class Verified(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_type = models.CharField(max_length=100, default='')


class Rating(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_type = models.CharField(max_length=100, default='')


class Active(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='')
    last_active_time = models.DateTimeField(auto_now=True)


class ProfilePicture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', null=True)
