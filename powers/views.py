from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Power
from .serializers import PowerSerializer
from heros_api.permissions import IsOwnerOrReadOnly


class PowerList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PowerSerializer
    queryset = Power.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PowerDetail(APIView):
    serializer_class = PowerSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            power = Power.objects.get(pk=pk)
            self.check_object_permissions(self.request, power)
            return power
        except Power.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        power = self.get_object(pk)
        serializer = PowerSerializer(
            power, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        power = self.get_object(pk)
        serializer = PowerSerializer(
            power, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
