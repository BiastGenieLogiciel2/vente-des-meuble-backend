from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Assurez-vous d'importer vos vues


urlpatterns = [
    path('', views.ProduitCreateView.as_view(), name='produits'),  # URL pour la création de produits
    path('<int:id>/', views.ProduitDetailView.as_view(), name='produit_detail'),  # URL pour les détails d'un produit
    path('update/<int:id>/', views.ProduitUpdateView.as_view(), name='produit_modifier'),  # URL pour modifier un produit existant
    path('delete/<int:id>/', views.ProduitDeleteView.as_view(), name='produit_supprimer'),  # URL pour supprimer un produit
]

# Configuration pour servir les fichiers médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
