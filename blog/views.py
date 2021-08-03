from django.shortcuts import render
from blog.models import Post


def post_list(request):
    posts = Post.objects.filter(status='published')
    return render(request, "blog/index.html",
                  {'posts': posts})
