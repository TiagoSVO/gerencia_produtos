from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='products', blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.subtitle}'

