from django.shortcuts import get_object_or_404, render
from .models import Post, Group


def index(request):
    post_list = Post.objects.select_related('author').all()
    context = {
        'posts': post_list,
    }
    return render(request, 'posts/index.html', context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.select_related('author').all()
    context = {
        'group': group,
        'posts': post_list,
    }
    return render(request, 'posts/group_list.html', context)
