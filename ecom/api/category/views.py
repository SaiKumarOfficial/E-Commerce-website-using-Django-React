from rest_framework import viewsets

from api.category.serializers import CategorySerializer
from api.category.models import Category
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
