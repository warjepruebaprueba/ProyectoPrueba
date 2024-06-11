from rest_framework import generics
from .models import *
from .serializers import *

class ListaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer
