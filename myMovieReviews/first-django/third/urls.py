from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('create/', views.create, name='movie-create'),
    path('update/', views.update, name='movie-update'),
    path('detail/', views.detail, name='movie-detail'),
    path('delete/', views.delete, name='movie-delete'),
]
