from django.contrib import admin

# Register your models here.
from django.contrib.admin import *

from blog.models import Blog, Image


class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 5

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin,]



