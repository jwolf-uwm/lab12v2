from django.db import models

# Create your models here.


class User(models.Model):
    user_username = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=50)


class Gift(models.Model):
    gift_name = models.CharField(max_length=100)
