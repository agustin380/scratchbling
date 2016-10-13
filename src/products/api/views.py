from rest_framework import viewsets, mixins

from .serializers import ProductsSerializer
from ..models import BackScratcher


class ProductsViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """
    This viewset automatically provides `list`, `create`,
    'retrieve` and `update` actions.
    """
    queryset = BackScratcher.objects.all()
    serializer_class = ProductsSerializer
