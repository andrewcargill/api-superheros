from django.http import Http404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.views.generic import ListView
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer
from heros_api.permissions import IsOwnerOrReadOnly


class PostList(ListView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    model = Post



class PostDetail(ListView):
    model = Post
    # serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # queryset = Post.all()

