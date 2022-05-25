from django.shortcuts import get_object_or_404, render
from .models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = f'Записи сообщества {group}'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
