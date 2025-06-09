from django.db import models

# Modèle représentant le classement des combattants
class Classement(models.Model):
    judokas = models.ForeignKey('judokas.Judokas', on_delete=models.CASCADE)
    point = models.IntegerField()
    classements = models.IntegerField()

    def __str__(self):
        return f"Classement de {self.judokas.nom}"