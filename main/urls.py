from django.urls import path

from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('study/',study,name='study'),
    path('blog/',blog,name='blog')

]