from django.shortcuts import render
from django.views.generic import DetailView, ListView

from blog.models import Blog



def index(request):
    return render(request,'index.html')


def study(request):
    return render(request,'study.html')

