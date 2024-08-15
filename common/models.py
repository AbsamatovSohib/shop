from django.db import models


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract=True


class Category(models.Model):
    name = models.CharField(max_length=127)
    photo = models.FileField(upload_to="media/documents/")

    def __str__(self):
        return self.name

class Storage(models.Model):
    size = models.IntegerField(default=32)


class Color(models.Model):
    color = models.CharField(max_length=200)


class ProductVariant(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    color = models.ForeignKey("Color", related_name="product_color", on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, related_name="product_storage", on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)


class Product(BaseModel):
    category = models.ForeignKey(Category, related_name="product_categories", on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    photo = models.FileField(upload_to="media/images/")
    in_cash = models.BooleanField(default=False)
    guarantee = models.CharField(max_length=128)
    producer = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name


class MainCharacterType(models.Model):
    name = models.CharField(max_length=32)


class Character(models.Model):
    product = models.ForeignKey(Product,related_name="product_main_character_type", on_delete=models.CASCADE)
    name = models.CharField(max_length=63)
    value = models.CharField(max_length=63)
    type = models.ForeignKey("MainCharacterType", related_name="character_type",
                             on_delete=models.CASCADE)


class ProductService(models.Model):
    name = models.CharField(max_length=63)
    product = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE)
    service_time = models.CharField(max_length=63)
    price_from = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name
    

class ProductServiceApplication(BaseModel):
    service = models.ForeignKey(ProductService, related_name="services", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=127)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.service.pk} -- {self.full_name}"


class FreeDiagnosisApply(models.Model):
    full_name = models.CharField(max_length=127)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.full_name}  -- {self.phone_number}"


class Discount(BaseModel):
    name = models.CharField(max_length=63)
    percentage = models.PositiveIntegerField(default=0)


class Customer(BaseModel):
    CHOICES = [
        ('person', "PERSON"),
        ('company', "COMPANY")
    ]

    name = models.CharField(max_length=63)
    photo = models.FileField(upload_to='media/documents/')
    type = models.CharField(max_length=7, choices=CHOICES, default="person")
    position = models.CharField(max_length=63)

    def __str__(self) :
        return self.name 

class FAQ(BaseModel):
    title = models.CharField(max_length=63)
    answer = models.TextField()


class Post(BaseModel):
    title = models.CharField(max_length=127)
    description = models.TextField()
    photo = models.ImageField(upload_to="media/images/")

    def __str__(self):
        return self.title


class Accessory(BaseModel):
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to="media/images/")

    def __str__(self) -> str:
        return self.title

class ComplexItems(models.Model):
    COMPLEX_TYPE = [
        ('vip', "VIP"),
        ('standard', "STANDARD"),
        ('mini', "MINI")
    ]

    product = models.ForeignKey(Product, related_name="complex_items_product", on_delete=models.CASCADE)
    accessories = models.ForeignKey(Accessory, related_name="complex_accessory", on_delete=models.CASCADE)
    discount_price = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=8, choices=COMPLEX_TYPE, default="vip")


class CardItems(models.Model):
    product_color = models.ForeignKey(ProductVariant, related_name="card_products", on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=0)
    card = models.ForeignKey("Card", related_name="card_item_product", on_delete=models.CASCADE)


class Card(BaseModel):
    CONNECTION_TYPE = [
        ('via_phone', "VIA_PHONE"),
        ('via_email', "VIA_EMAIL")
    ]

    PAYMENT_TYPES = [
        ('in cash', "IN_CASH"),
        ('via_card', "VIA_CARD"),
    ]

    promo_code = models.ForeignKey("PromoCode", related_name="promo_code_for", on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=127)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    connection_type = models.CharField(max_length=9, choices=CONNECTION_TYPE, default="via_phone")
    delivery = models.CharField(max_length=63)
    commentary = models.TextField()
    payment_type = models.CharField(max_length=15, choices=PAYMENT_TYPES, default="in cash")


class PromoCode(BaseModel):
    promo_code = models.CharField(max_length=10)
    discount_price = models.PositiveIntegerField(default=0)
    total_usage = models.PositiveIntegerField(default=1)
    min_bought_price = models.PositiveIntegerField(default=200)


class WareHouse(models.Model):
    product = models.ForeignKey(Product, related_name="warehouse_product", on_delete=models.CASCADE)
    total_quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)


class ComplexCardItems(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="complex_item_card")
    complex_item = models.ForeignKey(ComplexItems, on_delete=models.CASCADE, related_name="complex_item")
