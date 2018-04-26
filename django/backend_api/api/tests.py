#from django.test import TestCase
# This is now used for tutorial at https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-32fcf40231e5
# Create your tests here.

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Songs
from .serializers import SongsSerializer

class BaseViewTest(APITestCase):
	client = APIClient()

	@staticmethod
	def create_song(title="", artist=""):
		if title != "" and artist != "":
			Songs.objects.create(title=title, artist=artist)

	def setUp(self):
		#add test data
		self.create_song("Get Up and Drive Your Funky Soul", "James Brown")
		self.create_song("Times They Are a Changin", "Bob Dylan")
		self.create_song("Ain't No Grave", "Johnny Cash")
		self.create_song("Castles Made Of Sand", "Jimi Hendrix")

class GetAllSongsTest(BaseViewTest):
	"""
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
	"""
	#hit the API endpoint
	response = self.client.get(reverse("songs-all", kwargs={"version": "v1"}))
	#fetch data from db
	expected = Songs.objects.all()
	serialized = SongsSerializer(expected, many=True)
	self.assertEqual(response.data, serialized.data)
	self.assertEqual(response.status_code, status.HTTP_200_OK)