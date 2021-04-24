from rest_framework import serializers
from audioapp.models import Song, Podcast


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = (
            'id',
            'name',
            'duration',
            'upload_time'
        )


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = (
            'id',
            'name',
            'duration',
            'upload_time',
            'host',
            'participants'
        )
