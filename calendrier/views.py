from django.shortcuts import render, redirect, HttpResponse
from .models import Calendrier
from django.views import View
from .forms import CalendrierForm
from django.contrib import messages

# Vue fonctionnelle : affiche la liste des événements
def index(request, *args, **kwargs):
    liste_calendrier = Calendrier.objects.all()  # Récupère tous les événements
    context = {
        'calendriers': liste_calendrier,
        'titre': 'Titre calendrier',
    }
    return render(request, 'calendriers/indexCalendrier.html', context)

# Vue basée sur une classe : permet de créer un événement
class CreateCalendrier(View):
    # Affiche le formulaire vide
    def get(self, request, *args, **kwargs):
        form = CalendrierForm()
        return render(request, 'calendriers/create_calendrier.html', {'form': form})

    # Traite les données soumises par le formulaire
    def post(self, request, *args, **kwargs):
        form = CalendrierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Calendrier enregistré avec succès')
            return redirect('calendriers:indexCalendrier')
        else:
            messages.error(request, 'Erreur lors de l\'enregistrement du calendrier')
            return render(request, 'calendriers/create_calendrier.html', {'form': form})
