from django.shortcuts import render
from rest_framework import status, permissions,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action

# Create your views here.

# creation d'un API pour ajouter les utilisateurs en utilisant UserSerializer.
class UserCreateView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Utilisateur créé avec succès"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# creation des vues pour mettre à jour, supprimer et lister les utilisateurs. Utilisation des permissions de Django REST Framework pour restreindre ces vues aux administrateurs.

# Permission personnalisée pour les administrateurs
class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    # Lister tous les utilisateurs (admin uniquement)
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    # Récupérer les détails d'un utilisateur
    def retrieve(self, request, pk=None):
        user = self.get_object()
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # Mettre à jour un utilisateur (admin uniquement)
    def update(self, request, pk=None):
        user = self.get_object()
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Supprimer un utilisateur (admin uniquement)
    def destroy(self, request, pk=None):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)