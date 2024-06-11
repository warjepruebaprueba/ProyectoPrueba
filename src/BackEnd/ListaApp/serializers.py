from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Lista


class ListaSerializer(serializers.ModelSerializer):
    nombre_usuario = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = Lista
        fields = ['id', 'usuario', 'nombre_usuario', 'contenido' ,'pago' ,'pagado']
