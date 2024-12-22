from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, get_all_products, get_by_id_product


router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products', get_all_products, name='products'),
    path('products/<str:pk>', get_by_id_product, name='get_by_id_product'),
    
]
