from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *
from django.db.models import F


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
        fields = ("name", "id")


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


class AccessoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = ("title", 'photo', "price", "description")


class ComplexItemsListSerializer(serializers.ModelSerializer):
    accessories = AccessoryListSerializers(many=True, read_only=True)
    photo = serializers.CharField(source="product_variant.product.photo.url")

    class Meta:
        model = ComplexItems
        fields = ("total_price", "discount_price", "accessories", "photo")


class ColorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ("color", "id")


class StorageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ("size", "id")



class ProductVariantSerializer(serializers.ModelSerializer):
    colors = ColorListSerializer()
    storages = StorageListSerializer()

    class Meta:
        model = ProductVariant
        fields = ('colors', 'storages', "price", "pk" )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['price'] = instance.product.price + instance.colors.extra_price + instance.storages.extra_price

        return representation

class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ("name", "photo", "description","in_cash", "guarantee", 'producer', 'variants')


class CharactersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("name", "quantity", "pk")


class MainCharacterTypeSerializer(serializers.ModelSerializer):
    character_type = CharactersListSerializer('character_type', many=True)
    class Meta:
        model = MainCharacterType
        fields = ("name", "character_type", "pk")


class ProductVariantListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    selected_storage = serializers.IntegerField(write_only=True, required=False)
    selected_color = serializers.IntegerField(write_only=True, required=False)


    class Meta:
        model = ProductVariant
        fields  = ("name", "description",'photo', 'selected_color', 'selected_storage',
                   )

    def get_name(self, obj):
        return obj.product.name

    def get_photo(self, obj):
        return obj.product.photo.url

    def get_description(self, obj):
        return obj.product.description

    def get_adjusted_price(self, obj):
        selected_storage = self.context.get('storage_id')
        selected_color = self.context.get('color_id')

        price = obj.price

        if selected_storage == "2":
            price += 1000
            if selected_color in [1, 2]:
                price += 100
            elif selected_color in [3, 4]:
                price += 200
        elif selected_storage == "3":
            price += 1500
            if selected_color in [1, 2]:
                price += 100
            elif selected_color in [3, 4]:
                price += 200
        return price


class CardItemsSerializer(serializers.ModelSerializer):
    product_variant = serializers.CharField(source="product_variant.pk ")

    class Meta:
        model = CardItems
        fields = ("product_variant", )


# class CardSerializer(serializers.ModelSerializer):
#     card_item = CardItemsSerializer(source='card_items_set', many=True, read_only=True)
#
#     class Meta:
#         model = Card
#         fields = ("promo_code", "full_name", "phone_number", "email",
#                   "connection_type", "delivery", "commentary", "payment_type",
#                   "card_item")

class ProductVariantSerializer1(ModelSerializer):
    color = serializers.SerializerMethodField()
    storage = serializers.SerializerMethodField()

    def get_color(self, obj):
        if hasattr(obj, 'colors'):
            if hasattr(obj.colors.first(), 'color'):
                return str(obj.colors.first().color)

    def get_storage(self, obj):
        if hasattr(obj, 'storages'):
            if hasattr(obj.storages.first(), 'size'):
                return str(obj.storages.first())


    class Meta:
        model = ProductVariant
        fields = "__all__"

class ProductAllListSerializer(ModelSerializer):
    variants = ProductVariantSerializer1(many=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductCharacterSerializer(serializers.ModelSerializer):
    product_main_character_type = MainCharacterTypeSerializer(many=True)

    class Meta:
        model = Product
        fields = ("product_main_character_type", )


class ProductVariantItemSerializer(serializers.Serializer):
    product_variant_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class ProductVariantCostSerializer(serializers.Serializer):
    items = serializers.ListField(
        child=ProductVariantItemSerializer()
    )


class ProductVariantIDListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ("pk", )



class PromoCodeCheckerSerializer(serializers.ModelSerializer):
    promo_code = serializers.CharField(write_only=True)
    total = serializers.IntegerField(write_only=True)
    promo_id = serializers.IntegerField(read_only=True)
    discount = serializers.IntegerField(read_only=True)

    class Meta:
        model = PromoCode
        fields = ("promo_code", "total", "promo_id", "discount")

    def validate(self, attrs):
        promo = attrs['promo_code']
        total = attrs['total']

        try:
            promo_code = PromoCode.objects.get(promo_code=promo)
        except PromoCode.DoesNotExist:
            raise serializers.ValidationError({"promo_code": "Bunday promo kod mavjud emas"})

        if total <= promo_code.min_bought_price:
            raise serializers.ValidationError(
                {"total": "Umumiy qiymat promo kod ishlatilishi mumkin bo'lgan qiymatdan kam"})

        if promo_code.total_usage <= 0:
            raise serializers.ValidationError({"promo_code": "Promokoddan foydalanish soni tugagan"})

        attrs["promo_id"] = promo_code.pk
        attrs['discount'] = promo_code.discount_price

        return attrs


class CardItemsCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = CardItems
        fields = ("product_variant", "quantity")

class CreateOrderSerializer(serializers.ModelSerializer):
    card_items = CardItemsCreateSerializer(many=True, required=True, write_only=True)
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = ("promo_code", "full_name", "email", "connection_type", "delivery", "comment_type", "card_items", "pk",
                  "total_cost")


    def create(self, validated_data):
        card_items = validated_data.pop("card_items")
        instance = super().create(validated_data)

        for item in card_items:
            CardItems.objects.create(
                card=instance,
                **item
            )
        return instance

    def get_total_cost(self, card, *args, **kwargs):
        total = CardItems.objects.filter(card=card).aggregate(total=Sum(F("quantity") * F("product_variant__price")))["total"]
        if card.promo_code:
            total = total - card.promo_code.discount_price
        return total


# class TotalCostSerializer(serializers.ModelSerializer):
    # total_cost = serializers.SerializerMethodField()

    # class Meta:
    #     model = Card
    #     fields = ("total_cost", )

    # def get_total_cost(self, card, *args, **kwargs):
    #     total = CardItems.objects.filter(card=card).aggregate(total=Sum("total_price"))["total"]
    #     total = total - card.promo_code.discount_price
    #     return total
