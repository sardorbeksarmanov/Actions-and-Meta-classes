from django.contrib import admin
from .models import Albom, Artist, Songs, SongsAlbom

admin.site.register([Albom, Artist, Songs, SongsAlbom])
