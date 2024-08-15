from rest_framework import serializers
from .models import *


class FreeDiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeDiagnosisApply
        fields = ("full_name", "phone_number")

    def create(self, validated_data):
        return super().create(validated_data)


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", )


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", )


class ProductServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductService
        fields = ("name", "service_time", "price_from")


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("name", "position", "photo")


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("photo", )


class FAQListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ("title", "answer")


class CategoryWithPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "photo")


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "description", "photo", "pk")


class ProductServiceApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductServiceApplication
        fields = ("full_name", "phone_number", "service")

    def create(self, validated_data):
        return super().create(validated_data)


class CharacterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("name", "value", "type")


class AccessoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = ("title", 'photo', "price", "description")


class ComplexItemsListSerializer(serializers.ModelSerializer):
    accessories = AccessoryListSerializers(many=True, read_only=True)
    photo = serializers.CharField(source="product.photo")

    class Meta:
        model = ComplexItems
        fields = ("price", "discount_price", "accessories", "photo")

