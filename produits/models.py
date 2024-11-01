from django.db import models

class Produit(models.Model):
    # Champ pour le nom du produit
    nom = models.CharField(max_length=255, verbose_name="Nom du produit")
    
    # Champ pour le style de produit
    style = models.CharField(max_length=100, verbose_name="Style de produit")
    
    # Champ pour le matériau avec lequel il est fait
    materiau = models.CharField(max_length=100, verbose_name="Matériau")
    
    # Champ pour l'image descriptive du produit
    image = models.ImageField(upload_to='produits/', verbose_name="Image du produit")

    # Méthode pour retourner une représentation lisible du produit
    def __str__(self):
        return self.nom

    # Optionnel : vous pouvez ajouter des métadonnées pour le modèle
    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
