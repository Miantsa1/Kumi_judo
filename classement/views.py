from django.shortcuts import render, redirect, HttpResponse
from .models import Classement
from django.views import View
from .forms import ClassementForm
from django.contrib import messages

# Vue fonctionnelle : affiche la liste des classements
def index(request, *args, **kwargs):
    liste_classement = Classement.objects.all()  # Récupère tous les classements
    context = {
        'classements' : liste_classement
    }
    return render(request, 'classements/indexClassement.html', context)

# Vue basée sur une classe : permet de créer un calendrier
class CreateClassement(View):
        # Affiche le formulaire vide
    def get(self, request, *args, **kwargs):
        form = ClassementForm()
        return render(request, 'classements/create_classement.html', {"form": form})
    
        # Traite les données soumises par le formulaire
    def post(self, request, *args, **kwargs):
        form = ClassementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classement enregistré')
            return redirect('classements:indexClassement')

        else:
            messages.error(request, 'Erreur lors de l\'enregistrement du classement')
            return render(request, 'classements/create_classement', {'form': form})

    
