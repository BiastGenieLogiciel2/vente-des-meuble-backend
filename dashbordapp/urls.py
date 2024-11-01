# dashboardapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCreateView, UserViewSet

# Création d'un routeur pour enregistrer les routes de l'API
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

# Inclusion des routes pour créer et gérer les utilisateurs
urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user-create'),  # Route pour la création d'un utilisateur
    path('', include(router.urls)),  # Route pour lister, mettre à jour, et supprimer les utilisateurs
]
