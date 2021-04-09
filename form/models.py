from django.db import models
from phone_field import PhoneField




class Form(models.Model):
    choices = (
        ('python', 'Python'),
        ('javascript', 'Javascript'),
    )
    first_name= models.CharField(max_length=150,blank=True,null=True)
    last_name= models.CharField(max_length=150,blank=True,null=True)
    experience = models.TextField(blank=True,null=True)
    language = models.CharField(choices=choices,max_length=20,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    # phone = models.IntegerField(blank=True,null=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')


    def __str__(self):
        return f'{self.first_name} {self.last_name} '

