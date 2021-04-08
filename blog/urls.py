from django.urls import path

from .views import *

urlpatterns = [

    path('blog/',BlogPageView.as_view(),name='blog'),
    path('add_blog/', add_blog, name='add_blog'),
    path('update_blog/<int:pk>/', update_blog, name='update_blog'),
    path('delete_blog/<int:pk>/', DeleteBlogView.as_view(), name='delete_blog'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),

]