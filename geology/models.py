from django.db import models

class GeologicalHorizon(models.Model):
    name = models.CharField(max_length=20, verbose_name="Горизонт")  # НД-5, НД-15, ВД-13
    depth_min = models.IntegerField(verbose_name="Глибина min, м")
    depth_max = models.IntegerField(verbose_name="Глибина max, м")
    rock_type = models.CharField(max_length=200, verbose_name="Породи")
    gas_present = models.BooleanField(default=True, verbose_name="Газоносний")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Газоносний горизонт"
        verbose_name_plural = "Газоносні горизонти"

class TectonicFeature(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    map_image = models.ImageField(upload_to='tectonic/', blank=True)

class DensityVelocity(models.Model):
    age = models.CharField(max_length=50)  # Четвертинні, Неоген, Рифей
    lithology = models.CharField(max_length=100)
    depth_interval = models.CharField(max_length=50)
    density = models.FloatField(help_text="×10³ кг/м³")
    v_min = models.FloatField(blank=True, null=True, help_text="V min, м/с")
    v_max = models.FloatField(blank=True, null=True, help_text="V max, м/с")