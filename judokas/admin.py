from django.contrib import admin


# enregistrer les tables
from .models import Judokas

#admin.site.register(Produit) #ce n'est pas encore sous forme de tableau

#Pour qu'il s'affiche en tableau

@admin.register(Judokas) #mettre un decorateur
class JudokasAdmin(admin.ModelAdmin):
    list_display = ('nom' , 'prenom' , 'club' , 'cat_age', 'cat_poids', 'image' )
