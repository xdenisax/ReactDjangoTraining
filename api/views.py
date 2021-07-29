
from rest_framework import generics, serializers
from .serializers import RoomSerializer
from .models import Room

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


