from django.contrib import admin

# Register your models here.
from django.contrib.admin import *

from blog.models import Blog, Image,Comment


class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 5

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin,]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'date_added',)
    list_filter = ('date_added', 'date_updated')
    search_fields = ('user', 'body')