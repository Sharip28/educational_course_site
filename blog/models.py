from django.db import models

# Create your models here.
from account.models import User


class Blog(models.Model):
    title = models.CharField(max_length=150,blank=True)
    code = models.TextField(blank=True)
    detail = models.TextField(blank=True)

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blogs')
    created = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def get_image(self):
        return self.images.first()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'pk': self.pk})



class Image(models.Model):
    image = models.ImageField(upload_to='blogs',blank=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='images')

    def __str__(self):
        return self.image.url
