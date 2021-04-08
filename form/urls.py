from django.urls import path

from form.views import ApplicationView

urlpatterns = [
    path('form/', ApplicationView.as_view(), name='form'),

]
