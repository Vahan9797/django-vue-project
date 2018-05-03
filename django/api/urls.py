from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
	TokenObtainPairView,
	TokenRefreshView,
)

from .views import PostList, PostDetail, EchoView

urlpatterns = [
    path('', get_schema_view()),
    path('echo/', EchoView.as_view()),
	path('posts/', PostList.as_view()),
	path('posts/<int:pk>/', PostDetail.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/token/obtain/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
]