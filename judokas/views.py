from django.shortcuts import render, redirect, HttpResponse
from .models import Judokas
from django.views import View

from .forms import JudokasForm
from django.contrib import messages

# Vue fonctionnelle : affiche la liste des judokas
def index(request, *args, **kwargs):
    liste_judokas = Judokas.objects.all()
    context = {
        'judokas' : liste_judokas,
        'nom' : 'Nom du judokas',

    }
    return render(request, 'index.html', context)

# Vue basée sur une classe : permet de créer un judokas
class CreateJudokas(View):
    # Affiche le formulaire vide
    def get(self, request, *args, **kwargs):
        form = JudokasForm()
        return render(request, 'judokas/create_judokas.html', {'form': form})

    # Traite les données soumises par le formulaire
    def post(self, request, *args, **kwargs):
        form = JudokasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Judokas enregistré avec succès')
            return redirect('judokas:index')
        
        else:
            messages.error(request, 'Erreur lors de l\'enregistrement du judokas')
            return render(request, 'judokas/create_judokas.html', {'form': form})

