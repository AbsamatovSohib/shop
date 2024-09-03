from itertools import product
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializer import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404


class CategoryListApi(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryWithPhotoListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWithPhotoSerializer


class ProductNameListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]


class ProductServiceListAPI(generics.ListAPIView):
    queryset = ProductService.objects.all()
    serializer_class = ProductServiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["product"]


class FreeDiagnosisApplyCreateAPIView(generics.CreateAPIView):
    queryset = FreeDiagnosisApply.objects.all()
    serializer_class = FreeDiagnosisSerializer


class CustomerListAPI(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["type"]


class FAQListAPI(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQListSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class ProductServiceApplicationCreateAPIView(generics.CreateAPIView):
    queryset = ProductServiceApplication
    serializer_class = ProductServiceApplicationSerializer


class CategoryListWithPhotoAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWithPhotoSerializer


class ProductVariantDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductVariantLikedListAPIView(generics.ListAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer

    def get_queryset(self):
        return super().get_queryset().filter(is_liked=True)


class MainCharacterListAPIView(generics.ListAPIView):
    queryset = MainCharacterType
    serializer_class = MainCharacterTypeSerializer


class CharacterListAPIView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharactersListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["type"]

    def get_queryset(self):
        pk = self.kwargs["pk"]
        queryset = super().get_queryset()
        return queryset.filter(product_id=pk)


class ProductVariantFilterByListAPIView(generics.ListAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantListSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["size", "color", ]


class ComplexItemListAPIView(generics.ListAPIView):
    queryset = ComplexItems.objects.all()
    serializer_class = ComplexItemsListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["type"]


class CardItemsListAPiView(generics.ListAPIView):
    queryset = CardItems.objects.all()
    serializer_class = CardItemsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwuargs['pk']
        return queryset.filter(product_variant__product__pk=pk)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAllListSerializer


class ProductCharacterListAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCharacterSerializer
    lookup_field = "pk"

# class ProductVariantCostAPIView(generics.GenericAPIView):
#     serializer_class = ProductVariantCostSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             total_cost = 0
#             detailed_costs = []
#
#             for item in serializer.validated_data['items']:
#                 product_variant_id = item['product_variant_id']
#                 quantity = item['quantity']
#
#                 product_variant = get_object_or_404(ProductVariant, id=product_variant_id)
#
#                 cost = product_variant.price * quantity
#                 total_cost += cost
#
#                 detailed_costs.append({
#                     'product_variant': product_variant_id,
#                     'quantity': quantity,
#                     'cost': cost
#                 })
#
#             return Response({
#                 'total_cost': total_cost,
#                 'detailed_costs': detailed_costs
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductVariantPkListApiView(generics.ListAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantIDListSerializer


class PromoCodeCheckAPIView(generics.GenericAPIView):
    serializer_class = PromoCodeCheckerSerializer

    def post(self, request, *args, **kwargs):
        serializer = PromoCodeCheckerSerializer(data=request.data)
        if serializer.is_valid():
            promo_code_id = serializer.validated_data['promo_id']
            discount = serializer.validated_data['discount']

            return Response(
                {
                    "promo_code_id": promo_code_id,
                    "discount" : discount
                 },
                    status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateCardAPIView(generics.CreateAPIView):
    serializer_class =  CreateOrderSerializer


# class TotalCostAPIView(generics.RetrieveAPIView):
#     serializer_class = TotalCostSerializer
#     queryset = Card



