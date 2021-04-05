from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


class RegisterView(SuccessMessageMixin,CreateView):
    model = User
    template_name ='account'
