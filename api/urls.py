from django.urls import path, include
from rest_framework import routers
from .views import ArtistViewSetWeb, AlbomViewSetWeb, SongsViewSetWeb

router = routers.DefaultRouter()
# web
router.register(r'artists-web', ArtistViewSetWeb, basename='artists-web')
router.register(r'albom-web', AlbomViewSetWeb, basename='albom-web')
router.register(r'songs-web', SongsViewSetWeb, basename='songs-web')


urlpatterns = [
    path('', include(router.urls)),
]