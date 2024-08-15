from rest_framework import serializers
from api.models import Artist, Albom, Songs, SongsAlbom

# Web

class ArtistSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'first_name', 'last_name', 'username', 'image', 'listen', 'status']


class AlbomSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = ['id', 'artist', 'description', 'title', 'image', 'listen', 'status']


class SongSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['id', 'artist', 'title', 'description', 'image', 'listen', 'status']



class SongsAlbomSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = SongsAlbom
        fields = ['id', 'artist', 'songs']
