from rest_framework import serializers
from movies.models import ProductCategory

#Product category serializer
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
