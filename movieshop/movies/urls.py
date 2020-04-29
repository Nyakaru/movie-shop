from django.urls import path

from .views import ProductCategoryView, SingleProductCategoryView

app_name = 'movies'

urlpatterns = [
    path('categories', ProductCategoryView.as_view()),
    path('categories/<category_id>', SingleProductCategoryView.as_view()),
]
