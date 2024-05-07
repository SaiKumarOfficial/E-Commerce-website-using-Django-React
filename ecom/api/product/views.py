from rest_framework import viewsets
from api.product.models import Product
from api.product.serializers import ProductSerializer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset= Product.objects.all().order_by('id')
    serializer_class= ProductSerializer