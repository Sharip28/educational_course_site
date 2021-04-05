from django.db import models

# Create your models here.
from account.models import User


class Trello(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='trello')
    created = models.DateTimeField()

    def __str__(self):
        return self.title