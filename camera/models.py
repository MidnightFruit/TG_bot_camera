from django.db import models

from Users.models import User

NULLABLE = {"blank": True, "null": True}

class Camera(models.Model):
    name = models.CharField(max_length=64, verbose_name="название камеры")
    camera_url = models.URLField(**NULLABLE, verbose_name="ссылка на камеру")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="владелец камеры")

    class Meta:
        verbose_name = "камера"
        verbose_name_plural = "камеры"

