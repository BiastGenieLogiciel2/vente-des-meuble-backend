from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.validators import EmailValidator
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

# creation d'un user normal avec verification de la presence du nom et de l'email et normalisation du mots du passe
class UserManger(BaseUserManager):
    def create_user(self, email, nom, prenom, password=None):
        if not email:
            raise ValueError("L'utilisateur doit avoir un email valide")
        if not nom:
            raise ValueError("L'utilisateur doit avoir un nom")
        
        user = self.model(
            email = self.normalize_email(email),
            nom = nom,
            prenom = prenom
        )
        
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    # ceration du super admin
    def create_superuser(self, email, nom, prenom, password):
        user = self.create_user(
            email,
            nom=nom,
            prenom=prenom,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
  
  
    
class User(AbstractBaseUser):
    nom  = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(validators=[EmailValidator], unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    
    objects = UserManger()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom']
    
    
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('delivery', 'Livreur')
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.role}"

    @property
    def is_staff(self):
        return self.is_admin
