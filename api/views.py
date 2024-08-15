from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Artist, Albom, Songs, SongsAlbom
from .serializers import ArtistSerializerWeb, AlbomSerializerWeb, SongSerializerWeb
from rest_framework.response import Response

class ArtistViewSetWeb(viewsets.ModelViewSet):
    serializer_class = ArtistSerializerWeb

    def get_queryset(self):
        return Artist.objects.filter(status='pb')

    @action(detail=True, methods=["GET"])
    def listen(self, request, *args, **kwargs):
        artist = self.get_object()
        artist.listen += 1
        artist.save()
        return Response(data={"listened": artist.listen})

    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        artists = self.get_queryset().order_by("-listen")[:3]
        serializer = ArtistSerializerWeb(artists, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET", ])
    def null_listen(self, request, *args, **kwargs):
        artists = self.get_queryset().filter(listen=0)
        serializer = ArtistSerializerWeb(artists, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET", ])
    def all_listen(self, request, *args, **kwargs):
        artists = self.get_queryset()
        for artist in artists:
            artist.listen += 1
            artist.save()
        return Response(data={"message": "all artists listened"})

    @action(detail=False, methods=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        artists = self.get_queryset()
        for artist in artists:
            artist.pb_to_df()
        return Response(data={"message": "all artists changed to draft"})

    @action(detail=False, methods=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        artists = Artist.objects.all()
        for artist in artists:
            artist.df_to_pb()
        return Response(data={"message": "all artists changed to publish"})

    @action(detail=True, methods=["GET", ])
    def to_publish_d(self, request, *args, **kwargs):
        artist = self.get_object()
        artist.df_to_pb()
        return Response(data={"message": "artist changed to publish"})

    @action(detail=True, methods=["GET", ])
    def to_draft_d(self, request, *args, **kwargs):
        artist = self.get_object()
        artist.pb_to_df()
        return Response(data={"message": "artist changed to draft"})


class AlbomViewSetWeb(viewsets.ModelViewSet):
    serializer_class = AlbomSerializerWeb

    def get_queryset(self):
        return Albom.objects.filter(status='pb')

    @action(detail=True, methods=["GET"])
    def listen(self, request, *args, **kwargs):
        albom = self.get_object()
        albom.listen += 1
        albom.save()
        return Response(data={"listened": albom.listen})

    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        alboms = self.get_queryset().order_by("-listen")[:3]
        serializer = AlbomSerializerWeb(alboms, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET", ])
    def null_listen(self, request, *args, **kwargs):
        alboms = self.get_queryset().filter(listen=0)
        serializer = AlbomSerializerWeb(alboms, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET", ])
    def all_listen(self, request, *args, **kwargs):
        alboms = self.get_queryset()
        for albom in alboms:
            albom.listen += 1
            albom.save()
        return Response(data={"message": "all alboms listened"})

    @action(detail=False, methods=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        alboms = self.get_queryset()
        for albom in alboms:
            albom.pb_to_df()
        return Response(data={"message": "all alboms changed to draft"})

    @action(detail=False, methods=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        alboms = Albom.objects.all()
        for albom in alboms:
            albom.df_to_pb()
        return Response(data={"message": "all alboms changed to publish"})

    @action(detail=True, methods=["GET", ])
    def to_publish_d(self, request, *args, **kwargs):
        albom = self.get_object()
        albom.df_to_pb()
        return Response(data={"message": "albom changed to publish"})

    @action(detail=True, methods=["GET", ])
    def to_draft_d(self, request, *args, **kwargs):
        albom = self.get_object()
        albom.pb_to_df()
        return Response(data={"message": "albom changed to draft"})


class SongsViewSetWeb(viewsets.ModelViewSet):
    serializer_class = SongSerializerWeb

    def get_queryset(self):
        return Songs.objects.filter(status='pb')

    @action(detail=True, methods=["GET",])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        song.listen += 1
        song.save()
        return Response(data={"listened": song.listen})

    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        songs = self.get_queryset().order_by("-listen")[:3]
        serializer = SongSerializerWeb(songs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET", ])
    def null_listen(self, request, *args, **kwargs):
        songs = self.get_queryset().filter(listen=0)
        serializer = SongSerializerWeb(songs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET", ])
    def all_listen(self, request, *args, **kwargs):
        songs = self.get_queryset()
        for song in songs:
            song.listen += 1
            song.save()
        return Response(data={"message": "all songs listened"})

    @action(detail=False, methods=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        songs = self.get_queryset()
        for song in songs:
            song.pb_to_df()
        return Response(data={"message": "all songs changed to draft"})

    @action(detail=False, methods=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        songs = Songs.objects.all()
        for song in songs:
            song.df_to_pb()
        return Response(data={"message": "all songs changed to publish"})

    @action(detail=True, methods=["GET", ])
    def to_publish_d(self, request, *args, **kwargs):
        song = self.get_object()
        song.df_to_pb()
        return Response(data={"message": "song changed to publish"})

    @action(detail=True, methods=["GET", ])
    def to_draft_d(self, request, *args, **kwargs):
        song = self.get_object()
        song.pb_to_df()
        return Response(data={"message": "song changed to draft"})
