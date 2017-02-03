from django.db import models

# Create your models here.

class Genres(models.Model):
	"""Artists model class
		The purpose of this class is to define the Genres data model.
		author: Ike
		methods: __str__ Returns a string
		subclasses: Meta (with ordering by last_name)
	"""
	
	name = models.CharField(max_length=50, default='')

	def __str__(self):
		return '{} {} {} {} {} {} {}'.format(self.name)	

class Artists(models.Model):
	"""Artists model class
		The purpose of this class is to define the Artists data model.
		author: Ike
		methods: __str__ Returns a string
		subclasses: Meta (with ordering by last_name)
	"""
	
	first_name = models.CharField(max_length=50, default='')
	last_name = models.CharField(max_length =50)
	created_date = models.DateTimeField(auto_now_add=True)
	genres = models.ManyToMany(Genres)

	class Meta:
		ordering = ('last_name',)

	def __str__(self):
		return '{} {} {} {} {} {} {}'.format(self.first_name, self.last_name, self.created_date)


class Songs(models.Model):
	""" 
	Songs model class
	The purpose of this class is to define the Songs data model.
	author: Ike
	subclasses: Meta (with ordering by name)
	
	"""
	song_name = models.CharField(max_length=100)
	genre = models.ForeignKey(Genres, null=True)
	artists = models.ManyToMany(Artists)

	def __str__(self):
		return '{}'.format(self.song_name)

class Albums(models.Model):

	""" 
	Albums model class
	The purpose of this class is to define the Albums data model.
	author: Ike
	subclasses: Meta (with ordering by name)
	"""
	name = models.CharField(max_length=55)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	description = models.CharField(max_length=140)
	song_Id = models.ForeignKey(Songs, null=True)
	artists = models.ManyToMany(Artists)

	def __str__(self):
		return '{} {} {} {}'.format(self.name, self.price, self.description, self.song_Id, self.artists)
