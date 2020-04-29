from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import ProductCategory, Products
from .serializers import ProductCategorySerializer, ProductSerializer
from .validators import validate_category, validate_product

class ProductCategoryView(generics.ListCreateAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def post(self, request):
        category = request.data

        # Create an category from the above data
        serializer = self.serializer_class(data=category)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": "Category created successfully", 'category': serializer.data})

class SingleProductCategoryView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = ProductCategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

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

class ProductView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        product = request.data

        # Create an category from the above data
        serializer = self.serializer_class(data=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": "Product created successfully", 'product': serializer.data})

class SingleProductView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, product_id):
        
        product = validate_product(product_id)
        serializer = self.serializer_class(product)
        return Response({"product": serializer.data})

    def patch(self, request, product_id):
        product = validate_product(product_id)
        data = request.data
        serializer = self.serializer_class(instance=product, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": "Product updated successfully", 'product': serializer.data})

    def delete(self, request, product_id):
        product = validate_product(product_id)
        product.delete()
        
        return Response({"success": "Product deleted successfully"})
