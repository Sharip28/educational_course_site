from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    choices = (
        ('python','Python'),
        ('javascript','Javascript'),
    )


    email = models.EmailField(unique=True,blank=True,null=True)
    first_name = models.CharField(max_length=150,blank=True,null=True)
    last_name = models.CharField(max_length=150,blank=True,null=True)
    image = models.ImageField(upload_to='users',blank=True,null=True)
    group = models.CharField(choices=choices,max_length=20,blank=True,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.get_full_name()

# class Group(j/f)