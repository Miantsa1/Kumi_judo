from django import forms
from .models import Calendrier

# Formulaire basé sur le modèle Calendrier
class CalendrierForm(forms.ModelForm):
    class Meta:
        model = Calendrier
        # Champs du modèle à inclure dans le formulaire
        fields = ['titre', 'description', 'date_competiton', 'endroit']
