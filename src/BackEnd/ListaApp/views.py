from rest_framework import generics
from .models import *
from .serializers import *

class ListaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer



from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def create_admin_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_superuser(username=username, password=password)
        return Response({"message": "Admin user created successfully."}, status=status.HTTP_201_CREATED)
