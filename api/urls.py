from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from . import views

schema_view = get_schema_view(title='Blog API')
router = routers.DefaultRouter()

router.register('banner', views.BannerModelViewSet)
router.register('product', views.ProductModelViewSet)
router.register('product-gallery', views.ProductGalleryModelViewSet)
router.register('category', views.CategoryModelViewSet)
router.register('cart', views.CartModelViewSet)
router.register('cart_item', views.CartItemModelViewSet)
router.register('address', views.AddressModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('account/', include('rest_auth.urls')),
    path('account/registration/', include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title='Blog API')),
    path('schema/', schema_view),
]
