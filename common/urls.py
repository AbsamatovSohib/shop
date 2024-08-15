from django.urls import path
from common import views


urlpatterns = [
    path("category_list/", views.CategoryListApi.as_view(), name="category-list"),
    path("product-name-list/", views.ProductNameListAPI.as_view(), name="product-name-list"),
    path("product-service-list/", views.ProductServiceListAPI.as_view(), name="product-service-list"),
    path("product-service-application/", views.ProductServiceApplicationCreateAPIView.as_view(),
         name="product-service-application"),
    path("free-diagnosis-apply/", views.FreeDiagnosisApplyCreateAPIView.as_view(), name="free-diagnosis-apply"),
    path("customer/", views.CustomerListAPI.as_view(), name="customer-list"),
    path("faq-list/", views.FAQListAPI.as_view(), name="faq-list"),
    path("post-list/", views.PostListAPIView.as_view(), name="post-list"),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
]