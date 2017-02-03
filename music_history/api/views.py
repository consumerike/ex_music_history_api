from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from rest_framework import viewsets



class JSONResponse(HttpResponse):
    """
    author: Ike
    purpose: An HttpResponse that renders its content into JSON.
    Methods: __init__
        purpose: initialize a new instnce of JSON response
        arguments: 
        self- reference to the class instance being created
        data- request data
        kwargs- setting contenty type to application/json
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class GenresViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer

class ArtistsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer


class SongsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

class AlbumsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializer


