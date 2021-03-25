from django.urls import path 
from . import views 

urlpatterns=[
    path('', views.yt_download, name='Home'),
    path('progress', views.progreso, name='progress')
]