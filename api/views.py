from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import UserCreateSerializer, ProductDetailSerializer, ProductListSerializer
from .models import Product , Profile

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class ProductListAPIView(ListAPIView):
	queryset =  Product.objects.all()
	serializer_class = ProductListSerializer

class ProductDetailAPIView(RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'object_id'

class Profile(RetrieveAPIView):
	queryset = Profile.objects.all()

	def get_object(self):
		return Profile.objects.get(user = self.request.user)