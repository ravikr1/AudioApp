from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index1', views.index1, name='index1'),
    url(r'^api/songs$', views.song_list),
    url(r'^api/podcasts$', views.podcast_list),
]