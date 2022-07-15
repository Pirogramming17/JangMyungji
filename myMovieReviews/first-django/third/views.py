from django.shortcuts import render, get_object_or_404
from third.models import Movie
from django.core.paginator import Paginator
from third.forms import MovieForm
from django.http import HttpResponseRedirect

# Create your views here.
def list(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 5)

    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'movies': items
    }
    return render(request, 'third/list.html', context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/third/list/')
    form = MovieForm()
    return render(request, 'third/create.html', {'form': form})

def update(request):
    if request.method == 'POST':
        #item = Movie.objects.get(pk=request.POST.get('id'))
        item = get_object_or_404(Movie, pk=request.POST.get('id'))
        form = MovieForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
    elif request.method == 'GET':
        #item = Movie.objects.get(pk=request.GET.get('id'))
        item = get_object_or_404(Movie, pk=request.GET.get('id'))
        form = MovieForm(instance=item)
        return render(request, 'third/update.html', {'form': form})

    return HttpResponseRedirect('/third/list/')

def detail(request):
    if 'id' in request.GET:
        item = get_object_or_404(Movie, pk=request.GET.get('id'))
        return render(request, 'third/detail.html', {'item': item})

    return HttpResponseRedirect('/third/list/')

def delete(request):
    if 'id' in request.GET:
        item = get_object_or_404(Movie, pk=request.GET.get('id'))
        item.delete()

    return HttpResponseRedirect('/third/list/')
