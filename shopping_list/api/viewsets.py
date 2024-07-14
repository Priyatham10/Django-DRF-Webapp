from rest_framework import viewsets

from shopping_list.api.serializers import ShoppingItemSerializer
from shopping_list.models import ShoppingItem

class ShoppingItemViewSet(viewsets.ModelViewSet):
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer