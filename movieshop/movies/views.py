from rest_framework.response import Response
from rest_framework import generics, mixins

from .models import ProductCategory
from .serializers import ProductCategorySerializer
from .validators import validate_category

class ProductCategoryView(generics.ListCreateAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    
    def post(self, request):
        category = request.data

        # Create an category from the above data
        serializer = self.serializer_class(data=category)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({"success": "Category '{}' created successfully".format(category_saved.name)})

class SingleProductCategoryView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = ProductCategorySerializer

    def get(self, request, category_id):
        
        category = validate_category(category_id)
        serializer = self.serializer_class(category)
        return Response({"category": serializer.data})

    def patch(self, request, category_id):
        category = validate_category(category_id)
        data = request.data
        serializer = self.serializer_class(instance=category, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": "Category updated successfully", 'category': serializer.data})

    def delete(self, request, category_id):
        category = validate_category(category_id)
        category.delete()
        
        return Response({"success": "Category deleted successfully"})
