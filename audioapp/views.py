from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from audioapp.models import Song
from audioapp.models import Podcast
from audioapp.serializers import SongSerializer
from audioapp.serializers import PodcastSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def song_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        songs = Song.objects.all()
        print("obje: ",songs)
        songs_serializer = SongSerializer(songs, many=True)
        return JsonResponse(songs_serializer.data, safe=False)
    elif request.method == 'POST':
        songs_data = JSONParser().parse(request)
        song_serializer = SongSerializer(data=songs_data)
        if song_serializer.is_valid():
            song_serializer.save()
            return JsonResponse(song_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def podcast_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        podcast = Podcast.objects.all()
        print("obje: ",podcast)
        podcast_serializer = PodcastSerializer(podcast, many=True)
        return JsonResponse(podcast_serializer.data, safe=False)
    elif request.method == 'POST':
        podcast_data = JSONParser().parse(request)
        podcast_serializer = PodcastSerializer(data=podcast_data)
        if podcast_serializer.is_valid():
            podcast_serializer.save()
            return JsonResponse(podcast_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return HttpResponse("Hello, You are welcome to applicaiton!")


def index1(request):
    return HttpResponse("Hello111, You are welcome to applicaiton!")
