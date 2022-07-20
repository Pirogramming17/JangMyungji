from django.urls import path
from . import views

urlpatterns = [
    path('idea_manage', views.idea_manage),
    path('', views.landing),
]