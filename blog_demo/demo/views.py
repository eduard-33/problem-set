# demo/viwvs.py
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(requset):
    posts = Post.objects.all()
    return render(requset, "home.html", {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post-detail.html", {"post": post})