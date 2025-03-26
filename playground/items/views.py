# Create your views here.
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from playground.items.models import Item


class ItemViewSet(ModelViewSet):
    class ItemSerializer(ModelSerializer):
        class Meta:
            model = Item
            fields = "__all__"
    queryset = Item.objects.all()
    serializer_class = ItemSerializer