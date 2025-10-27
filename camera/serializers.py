from rest_framework import serializers

from camera.models import Camera


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'
        read_only_fields = ('owner',)
        