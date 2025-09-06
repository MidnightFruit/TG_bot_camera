from django.db import models

from Users.models import User

NULLABLE = {"blank": True, "null": True}

class Camera(models.Model):
    name = models.CharField(max_length=64, verbose_name="название камеры")
    camera_url = models.URLField(**NULLABLE, verbose_name="ссылка на камеру")

    class Meta:
        verbose_name = "камера"
        verbose_name_plural = "камеры"


class Gallery(models.Model):
    name = models.CharField(max_length=32, verbose_name="имя галереи")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="владелец галереи")
    description = models.CharField(**NULLABLE, max_length=1024, verbose_name="описание галереи")

class Image(models.Model):
    name = models.CharField(max_length=128, verbose_name="имя рисунка")
    description = models.CharField(**NULLABLE, max_length=1024, verbose_name="описание")
    image = models.ImageField(upload_to="media/", **NULLABLE, verbose_name="изображение")
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name="галерея к которой принадлежит изображение")
