from django.views.generic import DetailView, ListView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BlogForm, ImageForm
from django.forms import modelformset_factory
from datetime import timedelta
from .models import *
from django.db.models import Q
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone



class BlogPageView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     image = self.get_object().get_image
    #     context['images'] = self.get_object().images.exclude(id=image.id)
    #     return context

def add_blog(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if blog_form.is_valid() and formset.is_valid():
            blog = blog_form.save()

            for form in formset.cleaned_data:
                image = form['image']
                Image.objects.create(image=image, blog=blog)
            return redirect(blog.get_absolute_url())
    else:
        blog_form = BlogForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'add_blog.html', locals())

def update_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
    blog_form = BlogForm(request.POST or None, instance=blog)
    formset = ImageFormSet(request.POST or None, request.FILES or None, queryset=Image.objects.filter(blog=blog))
    if blog_form.is_valid() and formset.is_valid():
        blog = blog_form.save()
        for form in formset:
            image = form.save(commit=False)
            image.blog = blog
            image.save()
        return redirect(blog.get_absolute_url())
    return render(request, "update_blog.html", locals())

class DeleteBlogView(DeleteView):
    model = Blog
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('blog')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.add_message(request, messages.SUCCESS, 'Successfully deleted!')
        return HttpResponseRedirect(success_url)