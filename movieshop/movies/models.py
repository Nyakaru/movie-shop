from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
