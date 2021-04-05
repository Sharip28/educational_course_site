from django.views.generic import DetailView, ListView

from blog.models import Blog



class BlogPageView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     image = self.get_object().get_image
    #     context['images'] = self.get_object().images.exclude(id=image.id)
    #     return context