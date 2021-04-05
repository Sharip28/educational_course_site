from blog.models import Blog


def get_blogs(request):
    blogs = Blog.objects.all()
    return {'blogs':blogs}