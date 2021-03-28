from rest_framework import serializers

from . import models

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class AddressHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Address
        fields = [
            'customer',
            'district',
            'waymark',
            'address',
            'note',
        ]


class CustomerModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        exclude = [
            'last_login',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',
            'user_permissions',
            'password',
            'is_superuser',
        ]


class CategoryModelSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        depth = 1
        model = models.Category
        fields = ['id', 'name', 'children']

    def get_children(self, obj):
        return CategoryModelSerializer(obj.get_children(), many=True).data


class ProductGalleryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductGallery
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product

        exclude = [
            'created_at',
            'updated_at',
        ]


class CartModelSerializer(serializers.ModelSerializer):
    customer = CustomerModelSerializer(read_only=True)

    class Meta:
        model = models.Cart
        fields = ['id', 'customer']


class CartItemModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CartItem
        fields = '__all__'


class BannerModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Banner
        fields = '__all__'
