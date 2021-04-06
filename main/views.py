from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from account.models import User
from blog.models import Blog
from main.models import Week


def index(request):
    return render(request,'index.html')


# def study(request):
#     weeks = Week.objects.all()
#     return render(request,'study.html',context={'weeks':weeks})

class StudyPageView(ListView):
    model = Week
    template_name = 'study.html'
    context_object_name = 'weeks'
    paginate_by = 2

    def get_template_names(self):
        template_name = super(StudyPageView, self).get_template_names()
        search = self.request.GET.get('q')
        if search :
            template_name = 'search.html'
        return template_name

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('q')
        if search:
            context['weeks'] = Week.objects.filter(Q(name__icontains=search)|Q(description__icontains=search))
        else:
            context['weeks'] = Week.objects.all()
        return context






def kpi(request,slug):
    weeks = Week.objects.get(slug=slug)

    return render(request,'kpi.html',context={'weeks':weeks})



