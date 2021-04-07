from rest_framework import viewsets, permissions, response, status, filters
from rest_framework.generics import ListAPIView
from . import models
from . import serializers


class AddressModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AddressHyperlinkedModelSerializer
    queryset = models.Address.objects.all()
    permission_classes = (permissions.IsAuthenticated, )


class CategoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategoryModelSerializer
    queryset = models.Category.objects.filter(level=0)
    permission_classes = (permissions.AllowAny, )
    http_method_names = ['get']
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ProductModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductModelSerializer
    queryset = models.Product.objects.all()
    permission_classes = (permissions.AllowAny, )
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    http_method_names = ['get']


class ProductGalleryModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductGalleryModelSerializer
    queryset = models.ProductGallery.objects.all()
    permission_classes = (permissions.AllowAny, )
    http_method_names = ['get']


class ProductFilter(ListAPIView):
    serializer_class = serializers.ProductModelSerializer
    queryset = models.Product.objects.all()
    http_method_names = ['get']


class BannerModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BannerModelSerializer
    queryset = models.Banner.objects.all()
    permission_classes = (permissions.AllowAny, )
    http_method_names = ['get']


class CartModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CartModelSerializer
    queryset = models.Cart.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    def get_queryset(self):
        query = self.queryset.filter(customer__id=self.request.user.id)
        return query

    # def create(self, request, *args, **kwargs):
    #     carts = request.user.carts.all()
    #     if carts.count() and not carts.last().status == 'active':
    #         return carts.last()
    #     else:
    #         models.Cart.objects.create(customer=request.user)
    #     return response.Response(status=status.HTTP_200_OK)


class CartItemModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CartItemModelSerializer
    queryset = models.CartItem.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        query = models.CartItem.objects.filter(cart__customer=self.request.user)
        return query

