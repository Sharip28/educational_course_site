from django.urls import path

from .views import *

urlpatterns = [

    path('blog/',BlogPageView.as_view(),name='blog')

]