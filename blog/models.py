
from django.db import models

# Create your models here.
from account.models import User


class Blog(models.Model):
    title = models.CharField(max_length=150,blank=True,null=True)
    detail = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    created = models.DateTimeField()
    code = models.TextField(blank=True,null=True)
    favorites = models.ManyToManyField(User, related_name='favorite', blank=True)
    #like
    likes = models.ManyToManyField(User,related_name='likes',blank=True)
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    @property
    def get_image(self):
        return self.images.first()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'pk': self.pk})




class Image(models.Model):
    image = models.ImageField(upload_to='blogs',blank=True,null=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='images')
    def __str__(self):
        return self.image.url


class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User,max_length=255, on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return f'{self.post.title}-{self.user.username}'
