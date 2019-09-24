from django.urls import path
from .views import UserCreateAPIView, ProductListAPIView, ProductDetailAPIView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', ProductListAPIView.as_view(), name = 'list'),
    path('detail/<int:object_id>/', ProductDetailAPIView.as_view(), name='detail'),
]