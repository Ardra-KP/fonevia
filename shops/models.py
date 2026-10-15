from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    district = models.CharField(max_length=30, default="Malappuram")
    location = models.CharField(max_length=100, default="Manjeri")
    phone = models.CharField(max_length=15, default="9048123456")
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.8)
    speciality = models.CharField(max_length=100, default="All Models")
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.district}"