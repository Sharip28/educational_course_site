from django.db import models

# Create your models here.
from account.models import User


class Week(models.Model):
    slug = models.SlugField(primary_key=True,max_length=150)
    name = models.CharField(max_length=150)
    decription = models.CharField(max_length=150)
    kpi = models.FileField(blank=True,upload_to='kpi')
    schedule = models.FileField(blank=True,upload_to='schedule')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='week')

    def __str__(self):
        return self.slug
