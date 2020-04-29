from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

class Products(models.Model):
    title = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(ProductCategory, related_name='products', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
