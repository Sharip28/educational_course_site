from django.db import models

# Create your models here.
from account.models import User


class Week(models.Model):
    slug = models.SlugField(primary_key=True,max_length=150)

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150,blank=True)
    kpi = models.TextField(blank=True)
    schedule = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='weeks')
    class Meta:
        ordering =['name']

    def __str__(self):
        return self.slug

    @property
    def get_kpi(self):
        return self.kpi

    @property
    def get_schedule(self):
        return self.schedule
