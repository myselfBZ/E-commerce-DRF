from rest_framework import serializers 
from .models import CustomUser, Product, Like, Cart, Comment, Order
from django.contrib.auth.models import User


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'user',
            ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

class ProductSerializer(serializers.ModelSerializer):
    available = serializers.SerializerMethodField(read_only=True)
    owner = serializers.SerializerMethodField(read_only=True)
    like_number = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'like_number',
            'available',
            'owner',
            'number',
            'id'
        ]

    def get_available(self, obj):
        return obj.available()
    def get_owner(self, obj):
        try:
            return obj.owner.username
        except:
            return None
    def get_like_number(self, obj):
        return obj.like_number()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [
            'liked',
            ]

class CartSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Cart
        fields = [
            'user',
            'products'
        ]
    def get_products(self, obj):
        products = obj.product.all()
        product_title = [product.title for product in products]
        return product_title
    def get_user(self, obj):
        return obj.user.user.username
    
class CommnetSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    product = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Comment
        fields = [
            'user',
            'comment',
            'product',
            ]
    
    def get_user(self, obj):
        return obj.user.username
    def get_product(self, obj):
        return obj.product.title


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Order
        fields = [
            'user',
            'review'
        ]

    def get_user(self, obj):
        return obj.user.username
    
