from rest_framework import serializers
from movies.models import ProductCategory, Products

#Product category serializer
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

#Products serializer
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset = ProductCategory.objects.all(),
        error_messages = {'does_not_exist': 'Product category does not exist' }
    )
    class Meta:
        model = Products
        fields = '__all__'
    
    def get_category(self, obj):
        serializer = ProductCategorySerializer(obj.category)
        return serializer.data
    
    def to_representation(self, instance):
        category = self.get_category(instance)
        data = super(ProductSerializer, self).to_representation(instance)
        data['category'] = category
        return data
