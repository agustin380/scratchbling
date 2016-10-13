from rest_framework.serializers import ModelSerializer

from ..models import BackScratcher


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = BackScratcher
        fields = ['name', 'description', 'price', 'sizes']
