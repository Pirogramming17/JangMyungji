from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post_dev


class PostList(ListView):
    model = Post_dev
    template_name = 'dev_manage/devlist.html'
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post_dev
    template_name = 'dev_manage/dev_detail.html'