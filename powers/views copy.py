from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Power
from .serializers import PowerSerializer
from heros_api.permissions import IsOwnerOrReadOnly


class PowerList(APIView):

    def get(self, request):
        powers = Power.objects.all()
        serializer = PowerSerializer(
            powers, many=True, context={'request': request}
        )
        return Response(serializer.data)


class PowerDetail(APIView):
    serializer_class = PowerSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # returns profile
    def get_object(self, pk):
        try:
            power = Power.objects.get(pk=pk)
            self.check_object_permissions(self.request, power)
            return power
        except Power.DoesNotExist:
            raise Http404

    # checks owner
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

