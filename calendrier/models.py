from django.db import models

# Modèle représentant un événement de calendrier pour une compétition de judo
class Calendrier(models.Model):
    titre = models.CharField(max_length=200)  # Titre de l'événement
    description = models.TextField()  # Description de l'événement
    date_competiton = models.CharField(max_length=200)  # Date de la compétition (sous forme de texte)
    endroit = models.CharField(max_length=100)  # Lieu de la compétition
    date_publication = models.DateTimeField(auto_now_add=True)  # Date d'enregistrement automatique

    def __str__(self):
        return f"{self.titre}"  # Représentation textuelle d'un objet Calendrier
