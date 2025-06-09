from django import forms
from .models import Judokas

# Formulaire basé sur le modèle Judokas
class JudokasForm(forms.ModelForm):
    class Meta:
        model = Judokas
        # Champs du modèle à inclure dans le formulaire
        fields = ['nom', 'prenom', 'club', 'cat_age', 'cat_poids', 'image']
