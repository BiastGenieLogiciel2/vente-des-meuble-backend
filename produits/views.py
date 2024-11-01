from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Produit  # Assurez-vous d'importer votre modèle Produit
from django.http import JsonResponse  # Importez JsonResponse

# Vue pour créer un nouveau produit
class ProduitCreateView(View):
    def get(self, request):
        return JsonResponse({'route': 'bien', 'message': 'Produit créé avec succès!'}, status=200)

    def post(self, request):
        # form = ProduitForm(request.POST, request.FILES)  # Récupère les données du formulaire
        # if form.is_valid():  # Vérifie si le formulaire est valide
        #     form.save()  # Enregistre le nouveau produit
        #     return JsonResponse({'route': 'bien', 'message': 'Produit créé avec succès!'}, status=200)
        return JsonResponse({'route': 'erreur', 'message': 'Erreur dans le formulaire.'}, status=400)

# Vue pour modifier un produit existant
class ProduitUpdateView(View):
    def get(self, request, id):
        # produit = get_object_or_404(Produit, id=id)  # Récupère le produit à modifier
        # form = ProduitForm(instance=produit)  # Crée une instance du formulaire avec les données du produit
        return JsonResponse({'route': 'erreur', 'message': 'Erreur dans le formulaire.'}, status=400)

    def post(self, request, id):
        # produit = get_object_or_404(Produit, id=id)  # Récupère le produit à modifier
        # form = ProduitForm(request.POST, request.FILES, instance=produit)  # Récupère les données du formulaire
        # if form.is_valid():  # Vérifie si le formulaire est valide
        #     form.save()  # Enregistre les modifications
        return JsonResponse({'route': 'bien', 'message': 'Produit modifié avec succès!'}, status=200)

# Vue pour afficher les détails d'un produit
class ProduitDetailView(View):
    def get(self, request, id):
        # produit = get_object_or_404(Produit, id=id)  # Récupère le produit par son ID
        # data = {
        #     'id': produit.id,
        #     'nom': produit.nom,
        #     'style': produit.style,
        #     'materiau': produit.materiau,
        #     'image': produit.image.url if produit.image else None  # Gérer l'absence d'image
        # }
        return JsonResponse({'route': 'bien', 'produit': 'toto'}, status=200)  # Renvoie un JSON avec les détails du produit

# Vue pour supprimer un produit existant
class ProduitDeleteView(View):

    def get(self, request, id):
        # produit = get_object_or_404(Produit, id=id)  # Récupère le produit par son ID
        # produit.delete()  # Supprime le produit
        return JsonResponse({'route': 'bien', 'message': 'Produit supprimé avec succès!'}, status=200)

    def post(self, request, id):
        # produit = get_object_or_404(Produit, id=id)  # Récupère le produit par son ID
        # produit.delete()  # Supprime le produit
        return JsonResponse({'route': 'bien', 'message': 'Produit supprimé avec succès!'}, status=200)
