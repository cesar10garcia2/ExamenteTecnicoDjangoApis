from rest_framework import serializers
from .models import Producto, Categoria



class CatagoriaProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','nombre']

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CatagoriaProductosSerializer()
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio','categoria']

