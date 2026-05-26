from django.db import models

class Seismic3DParams(models.Model):
    param_name = models.CharField(max_length=200, verbose_name="Параметр")
    value = models.CharField(max_length=100, verbose_name="Значення")
    unit = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.param_name}: {self.value} {self.unit}"

    class Meta:
        verbose_name = "Параметр 3D"
        verbose_name_plural = "Параметри 3D"

class FoldMapImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fold_maps/')
    description = models.TextField(blank=True)