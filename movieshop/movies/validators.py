from rest_framework.serializers import ValidationError

from .models import ProductCategory, Products

def validate_category(category_id):
    try:
        category = ProductCategory.objects.get(id=category_id)
        return category
    except ProductCategory.DoesNotExist:
        raise ValidationError('Category does not exist')

def validate_product(product_id):
    try:
        product = Products.objects.get(id=product_id)
        return product
    except Products.DoesNotExist:
        raise ValidationError('Product does not exist')
