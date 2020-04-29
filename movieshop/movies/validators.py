from rest_framework.serializers import ValidationError

from .models import ProductCategory

def validate_category(category_id):
    try:
        category = ProductCategory.objects.get(id=category_id)
        return category
    except ProductCategory.DoesNotExist:
        raise ValidationError('Category id does not exist')
