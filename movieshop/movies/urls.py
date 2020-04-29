from django.urls import path

from .views import ProductCategoryView, SingleProductCategoryView, ProductView, SingleProductView

app_name = 'movies'

urlpatterns = [
    path('categories', ProductCategoryView.as_view()),
    path('categories/<category_id>', SingleProductCategoryView.as_view()),
    path('products', ProductView.as_view()),
    path('products/<product_id>', SingleProductView.as_view()),
]
