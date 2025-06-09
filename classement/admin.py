from django.contrib import admin

from .models import Classement

# Enregistre le modèle Classement dans l'interface d'administration Django
@admin.register(Classement)
class ClassementAdmin(admin.ModelAdmin):
    # Colonnes à afficher dans la liste des objets Classement dans l'admin
    list_display = ('judokas','point', 'classements')
