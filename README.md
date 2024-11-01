# environement virtuelle
python -m venv venv

# tu source
cd venv/Scripts

activate

# tu rentre
cd ../..

# tu install tous les dependances
pip install -r .\requirements.txt

# tu demarre ton serveur
python manage.py runserver

# pour creer une nouvelle application regarde attentivement comment j'ai fait le elements de produit la pour te guider

- Creer une application produits

- tu construit le fichier urls.py ou tu configure les route pour ton produits

- tu importe cela dans le fichier urls.py du projet principale AMO 
    * path('produits/', include('produits.urls')),  # Inclut les URLs de l'application produits

- tu creer les differente vue dans le fichier view, (La vu detaille, creer et editer)

- tu peut utiliser une application pour teste ces api en get comme en post.

# liste des api a tester 

1 - http://127.0.0.1:8000/produits/ (la liste des produit)
2 - http://127.0.0.1:8000/produits/2 (Consulter le produit numero 2)
3 - http://127.0.0.1:8000/produits/update/1 (Modifier le produit numero 1)
3 - http://127.0.0.1:8000/produits/delete/2 (Suprimmer le produit numero 2)

pour tester ces api, tu peut utiliser les application connue tel que :
- insomnia
- postman
- restman
- ou tout simplement ton navigateur