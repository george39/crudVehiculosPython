from django.db import models

# Create your models here.


class Page(models.Model):
    brand = models.CharField(max_length=50, verbose_name="marca")
    line = models.CharField(max_length=50, verbose_name="linea")
    color = models.CharField(max_length=50, verbose_name="color", default='null')
    detail = models.CharField(max_length=50, verbose_name="detalles", default='null')
    price = models.DecimalField(max_digits=50, decimal_places=2, verbose_name="precio")
    visible = models.BooleanField(default='null')
    created_at = models.DateTimeField(auto_now=True)
