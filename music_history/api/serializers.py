from rest_framework import serializers
from bangazon_api.models import *



class GenresSerializer(serializers.HyperlinkedModelSerializer):
    """
    purpose: convert complex data
    into native python datatypes for JSON
    rendering
    author: Ike
    methods and subclasses: meta
        model: Genres from models.py
        fields: all fields from Genres data model are included
    """
    #Use of hyperlink serializer requires context to be a parameter when instantiating
    class Meta:
        model = Genres
        fields = '__all__'


class ArtistsSerializer(serializers.HyperlinkedModelSerializer):
    """ 
    Purpose: Artists complex data conversion
    The purpose of this class is to convert the Products data model to Json.
    author: Ike
    subclasses: Meta (contains fields that are to be converted)
    
    """
    class Meta:
        model = Artists
        fields = '__all__'

class SongsSerializer(serializers.HyperlinkedModelSerializer):
    """ 
    SongsSerializer class
    The purpose of this class is to convert the Categories data model to Json.
    author: Ike
    subclasses: Meta (contains fields that are to be converted)
    
    """

    class Meta:
        model = Songs
        fields = '__all__'

class AlbumsSerializer(serializers.HyperlinkedModelSerializer):
	""" purpose: convert model to JSON format
		author: Ike
		methods: Meta
		Class: Orders
		Fields: Include all 
	"""
	class Meta:
		model = Albums
		fields = '_all__'

