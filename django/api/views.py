#from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
# Create your views here.
from .models import Post
from .serializers import PostSerializer, MessageSerializer

class PostList(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class EchoView(RetrieveAPIView):
	def post(self, request, *args, **kwargs):
		serializer = MessageSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		return Response(serializer.data, status=status.HTTP_201_CREATED)