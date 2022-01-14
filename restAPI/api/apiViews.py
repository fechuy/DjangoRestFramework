from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Producto
from .serializers import ProductSerializer

class ProductList(APIView):
    def get(self, req):
        prod = Producto.objects.all()[:20]
        data = ProductSerializer(prod, many = True).data
        return Response(data)

class ProductDetalle(APIView):
    def get(self, req, pk):
        prod = get_object_or_404(Producto, pk=pk)
        data = ProductSerializer(prod).data
        return Response(data)