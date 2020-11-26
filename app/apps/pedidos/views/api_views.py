from django.http import Http404
from rest_framework import generics
from ..serializers import ProductoSerializer,CatagoriaProductosSerializer
from ..models import Producto, Categoria
from rest_framework.response import Response
from rest_framework.views import APIView


class ApiProductoList(generics.ListAPIView):
    serializer_class = ProductoSerializer
    def get_queryset(self):
        """
        Obtener una lista de productos con filtrado por categoria o nombre
        """
        nombre = self.request.GET.get('nombre')
        categoria = self.request.GET.get('categoria')
        if nombre == None:
            nombre = ''
        if categoria == None:
            categoria = ''
        object_list = Producto.objects.filter(
            nombre__icontains=nombre).filter(
            categoria__nombre__icontains=categoria).order_by('nombre')
        return object_list



class ApiProductoDetail(APIView):
    """
    Obtiene el detalle del producto
    """
    def get_object(self, pk):
        try:
            return Producto.objects.filter(estado=1).get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)


class ApiCatagoriaProductosList(generics.ListAPIView):
    serializer_class = CatagoriaProductosSerializer
    def get_queryset(self):
        """
        Obtiene las categorias de los productos
        """
        nombre = self.request.GET.get('nombre')
        if nombre == None:
            nombre = ''
        object_list = Categoria.objects.filter(
            nombre__icontains=nombre).order_by('nombre')
        return object_list
