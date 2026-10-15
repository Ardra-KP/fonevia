from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=200)

def __str__(self):
    return self.name

class Repair(models.Model):
    Order_id = models.CharField(max_length=200)
    Phone_model = models.CharField(max_length=200)
    issue = models.CharField(max_length=200)
    shop = models.ForeignKey('shops.Shop', on_delete=models.CASCADE)
    Status = models.CharField(max_length=200, default= "Repairing")
    Progress = models.DecimalField(max_digits=3, decimal_places=2, default=60)

def __str__(self):
    return self.Order_id