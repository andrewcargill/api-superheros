from django.http import Http404
from rest_framework import status, permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from rest_framework import generics, permissions
from .serializers import PostSerializer
from heros_api.permissions import IsOwnerOrReadOnly

#list of posts
class PostList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [
        filters.SearchFilter
    ]
    search_fields = [
        'caption',
        'owner__username'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        

# single post view
class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
   

    # permission_classes = [IsOwnerOrReadOnly]
    # serializer_class = PostSerializer

    # def get_object(self, pk):
    #     try:
    #         post = Post.objects.get(pk=pk)
    #         self.check_object_permissions(self.request, post)
    #         return post
    #     except Post.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk):
    #     post = self.get_object(pk)
    #     serializer = PostSerializer(
    #         post, context={'request': request}
    #     )
    #     return Response(serializer.data)

    # # editing posts 
    # def put(self, request, pk):
    #     post = self.get_object(pk)
    #     serializer = PostSerializer(
    #         post, data=request.data, context={'request': request}
    #     )
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         serializer.errors, status=status.HTTP_400_BAD_REQUEST
    #     )

    # # delete a post
    # def delete(self, request, pk):
    #     post = self.get_object(pk)
    #     post.delete()
    #     return Response(
    #         status=status.HTTP_204_NO_CONTENT
    #     )

