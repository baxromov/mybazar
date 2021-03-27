from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register('customer', views.CustomerModelViewSet)
router.register('address', views.AddressModelViewSet)
router.register('category', views.CategoryModelViewSet)
router.register('product', views.ProductModelViewSet)
router.register('cart', views.CartModelViewSet)
router.register('cart_item', views.CartItemModelViewSet)


urlpatterns = [
    path('', include(router.urls))
]
