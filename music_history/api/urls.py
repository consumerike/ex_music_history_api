"""This is the URL pattern for the api app"""
from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'genres', views.GenresViewSet)
router.register(r'artists', views.ArtistsViewSet)
router.register(r'songs', views.SongsViewSet)
router.register(r'albums', views.AlbumsViewSet)


#Wires up the API using auto URL routing.
#Includes login URLs for the browsable API
urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]