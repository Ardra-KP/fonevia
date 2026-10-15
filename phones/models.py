from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Apple, Samsung, Realme only

    def __str__(self):
        return self.name

class Phone(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='phones')
    model_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ram = models.CharField(max_length=20, default="8GB")
    storage = models.CharField(max_length=20, default="128GB")
    stock = models.IntegerField(default=10)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand.name} {self.model_name}"