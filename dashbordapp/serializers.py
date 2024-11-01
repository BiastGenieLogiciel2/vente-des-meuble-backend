# verification des donnees valide avant enregistrement

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    # confirguration de la validation du mots de passe 
    password = serializers.CharField(write_only=True, required=True)
    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['nom', 'prenom', 'email', 'password', 'password_confirmation']
    
    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("Les mots de passe ne correspondent pas.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        user = User(
            email=validated_data['email'],
            nom=validated_data['nom'],
            prenom=validated_data['prenom']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
# gestion des modifications, suppressions et affichages des utilisateurs.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'nom', 'prenom', 'role']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'nom', 'prenom', 'role']