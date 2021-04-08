from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect


from .forms import BlogForm, ImageForm,CommentForm
from django.forms import modelformset_factory
from datetime import timedelta
from .models import *
from django.db.models import Q
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.utils import timezone

from .permissions import UserHasPermissionMixin


class BlogPageView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'

    def get_template_names(self):
        template_name = super(BlogPageView, self).get_template_names()
        search = self.request.GET.get('q')
        filter = self.request.GET.get('filter')
        if search:
            template_name = 'searchblog.html'
        if filter:
            template_name = 'new_blog.html'
        return template_name

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('q')
        filter = self.request.GET.get('filter')
        if filter:
            start_date = timezone.now() - timedelta(hours=5)
            context['blogs'] = Blog.objects.filter(created__gte=start_date)
        if search:
            context['blogs'] = Blog.objects.filter(Q(title__icontains=search) | Q(detail__icontains=search))
        else:
            context['blogs'] = Blog.objects.all()
        return context

@login_required(login_url='login')
def add_blog(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if blog_form.is_valid() and formset.is_valid():
            blog = blog_form.save(commit=False)
            blog.user = request.user
            blog.save()


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
    if request.user == blog.user:
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
    else:
        return HttpResponse("<h1>You cant update other's posts!<h1>")


class DeleteBlogView(UserHasPermissionMixin,DeleteView):
    model = Blog
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('blog')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.add_message(request, messages.SUCCESS, 'Successfully deleted!')
        return HttpResponseRedirect(success_url)

def blog_detail(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    image = blog.get_image
    images = blog.images.exclude(id = image.id)
    comments = blog.comments.all()
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user

            # Assign the current post to the comment
            new_comment.post = blog
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    favorited = False
    liked = False
    if blog.favorites.filter(id=request.user.id).exists():
        favorited = True
    if blog.likes.filter(id=request.user.id).exists():
        liked = True
    number_of_likes = blog.total_likes()
    post_is_liked = liked
    return render(request,'blog_detail.html',locals())

def favorite_blog(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    if blog.favorites.filter(id=request.user.id).exists():
        blog.favorites.remove(request.user)
    else:
        blog.favorites.add(request.user)
    return redirect('blog_favorite_list')

def blog_favorite_list(request):
    user = request.user
    favorite_blogs = user.favorite.all()
    return render(request,'blog_favorite_list.html',locals())

def likeblog(request,pk):
    blog = get_object_or_404(Blog,id=pk)
    if blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
    else:
        blog.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail',args=[str(pk)]))





# class BlogDetailView(DetailView):
#     model = Blog
#     template_name = 'blog_detail.html'
#     context_object_name = 'blog'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         image = self.get_object().get_image
#         context['images'] = self.get_object().images.exclude(id=image.id)
#         return context





