from django.contrib import admin
from .models import Calendrier

# Enregistre le modèle Calendrier dans l'interface d'administration Django
@admin.register(Calendrier)
class CalendrierAdmin(admin.ModelAdmin):
    # Colonnes à afficher dans la liste des objets Calendrier dans l'admin
    list_display = ('titre', 'description', 'date_competiton', 'endroit', 'date_publication')
