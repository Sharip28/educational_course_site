from django.contrib.messages.views import SuccessMessageMixin
from django.forms import ModelForm
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from form.forms import ApplicationForm
from form.models import Form

#
class ApplicationView(SuccessMessageMixin,CreateView):
    model = Form
    template_name ='form/form.html'
    form_class = ApplicationForm
    success_url = reverse_lazy('home')
    success_message = 'Congratulations,you successfully sended your application!'