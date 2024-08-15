from rest_framework import generics
from .serializer import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend


class CategoryListApi(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


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


