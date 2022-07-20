from django import forms
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'idea_list/idea_list.html'
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post
    template_name = 'idea_list/idea_detail.html'

def creat(request):
    return render(request, 'idea_list/create.html', {'form' : forms})

# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(
#         request, 
#         'idea_list/index.html',
#         {
#             'posts': posts,
#         }
#         )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(
#         request,
#         'idea_list/single_page.html',
#         {
#             'post' : post,
#         }
#     )

 