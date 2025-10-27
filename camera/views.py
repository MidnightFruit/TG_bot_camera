from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView,\
      UpdateAPIView, DestroyAPIView
from camera.models import Camera
from camera.serializers import CameraSerializer


class CameraCreateAPIView(CreateAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CameraListAPIView(ListAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

    def get_queryset(self):
        return Camera.objects.filter(owner=self.request.user)
    
class CameraUpdateAPIView(UpdateAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

    def get_queryset(self):
        return Camera.objects.filter(owner=self.request.user)
    
class CameraRetrieveAPIView(RetrieveAPIView):
    serializer_class = CameraSerializer

    def get_queryset(self):
        return Camera.objects.filter(owner=self.request.user)
    
class CameraDestroyAPIView(DestroyAPIView):
    serializer_class = CameraSerializer

    def get_queryset(self):
        return Camera.objects.filter(owner=self.request.user)
    
