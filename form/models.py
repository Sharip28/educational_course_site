from django.db import models

# Create your models here.
from account.models import User


class Form:
    choices = (
        ('python', 'Python'),
        ('javascript', 'Javascript'),
    )
    first_name= models.CharField(max_length=150)
    last_name= models.CharField(max_length=150)
    experience = models.TextField(blank=True)
    language = models.CharField(choices=choices,max_length=20,blank=True)
    email = models.EmailField()
    phone = models.IntegerField()


    def __str__(self):
        return self.get_full_name()