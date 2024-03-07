from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _

# Create your models here.
class Parent(models.Model):
    cne=models.CharField(max_length=10)
    nom=models.CharField(max_length=10)
    prenom=models.CharField(max_length=10)
    genre=models.CharField(max_length=2)
    email=models.CharField(max_length=200)
    telephone=models.CharField(max_length=15)

class Professeur(models.Model):
    cne = models.CharField(max_length=10)
    nom=models.CharField(max_length=10)
    prenom=models.CharField(max_length=10)
    genre=models.CharField(max_length=2)
    email=models.CharField(max_length=200)
    telephone=models.CharField(max_length=15)
    salaire=models.FloatField()

class Filiere(models.Model):
    nomeF=models.CharField(max_length=30)

class Etudiant(models.Model):
        cne = models.CharField(max_length=10)
        nom = models.CharField(max_length=10)
        prenom = models.CharField(max_length=10)
        genre = models.CharField(max_length=2)
        email = models.CharField(max_length=200)
        telephone = models.CharField(max_length=15)
        groupe = models.CharField(max_length=3)
        niveau = models.CharField(max_length=15)
        father = models.ForeignKey(Parent, on_delete=models.CASCADE)
        filiere=models.ForeignKey(Filiere, on_delete=models.CASCADE)
        
class Cour(models.Model):
    nomCour=models.CharField(max_length=30)
    heureDebut=models.TimeField()
    heureFin=models.TimeField()

class Salle(models.Model):
    nomSalle=models.CharField(max_length=4)
    etage=models.IntegerField()
    TypeSalle=models.CharField(max_length=10)
class Presence_Cour(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cour = models.ForeignKey(Cour, on_delete=models.CASCADE)
    date_presence=models.DateField()
class Salle_Cour(models.Model):
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    cour = models.ForeignKey(Cour, on_delete=models.CASCADE)
    date_cour = models.DateField()

class users(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    role=models.CharField(max_length=15)

class User(AbstractUser):
    role = models.CharField(max_length=15)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='recette_users' 
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='recette_users_permissions'
    )