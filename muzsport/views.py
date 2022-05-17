from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from muzsport.models import Order
from muzsport.serializers import OrderSerializers


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializers
    queryset = Order.objects.all()
