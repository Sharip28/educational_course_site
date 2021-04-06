from django.urls import path


from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('study/',StudyPageView.as_view(),name='study'),
    path('kpi/<str:slug>/', kpi,name='kpi')

]