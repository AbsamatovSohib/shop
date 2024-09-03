from django.urls import path
from common import views


urlpatterns = [
    path("category-list/", views.CategoryListApi.as_view(), name="category-list"),
    path("category-list-with-photo/", views.CategoryWithPhotoListAPIView.as_view(), name="category-list-photo"),

    path("product-name-list/", views.ProductNameListAPI.as_view(), name="product-name-list"),
    path("product-service-list/", views.ProductServiceListAPI.as_view(), name="product-service-list"),
    path("product-service-application/", views.ProductServiceApplicationCreateAPIView.as_view(),
         name="product-service-application"),
    path("product/<int:pk>/", views.ProductVariantDetailAPIView.as_view()),

    path("free-diagnosis-apply/", views.FreeDiagnosisApplyCreateAPIView.as_view(), name="free-diagnosis-apply"),
    path("customer/", views.CustomerListAPI.as_view(), name="customer-list"),
    path("faq-list/", views.FAQListAPI.as_view(), name="faq-list"),

    path("post-list/", views.PostListAPIView.as_view(), name="post-list"),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),

    path("main-character-list/", views.MainCharacterListAPIView.as_view()),
    path("character-list/<int:pk>/", views.CharacterListAPIView.as_view()),

    path("product-variants-list/", views.ProductVariantFilterByListAPIView.as_view()),
    path("product-variant-pk-list/", views.ProductVariantPkListApiView.as_view()),
    path("complex-item-list/", views.ComplexItemListAPIView.as_view()),

    path('products/', views.ProductListAPIView.as_view()),
    path("product-character/<int:pk>/", views.ProductCharacterListAPIView.as_view()),
    path("product-liked-list/", views.ProductVariantLikedListAPIView.as_view()),

    path("check-promo/", views.PromoCodeCheckAPIView.as_view()),
    path("create-card/", views.CreateCardAPIView.as_view()),

    # path("product-variant-total/<int:pk>/", views.TotalCostAPIView.as_view())
]
