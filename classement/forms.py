from django import forms
from .models import Classement

# Formulaire basé sur le modèle Classement
class ClassementForm(forms.ModelForm):
    class Meta:
        model = Classement
        # Champs du modèle à inclure dans le formulaire
        fields = ['judokas', 'point', 'classements']