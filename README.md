# Kumi_judo
Cette application vise à simplifier la gestion des activités de la Fédération Malagasy de Judo, à assurer le suivi des performances des combattants, et à permettre l’accès au calendrier des compétitions à venir.


# Créer un projet avec django
django-admin startproject Kumi_Judo

# Structure du code avec django
# Kumi_Judo
# |__ /calendrier
#     |__ /admin.py
#     |__ /apps.py
#     |__ /forms.py
#     |__ /models.py
#     |__ /tests.py
#     |__ /urls.py
#     |__ /views.py

# |__ /classement
#     |__ /admin.py
#     |__ /apps.py
#     |__ /forms.py
#     |__ /models.py
#     |__ /tests.py
#     |__ /urls.py
#     |__ /views.py
# |__ /image
# |__ /judokas
#     |__ /admin.py
#     |__ /apps.py
#     |__ /forms.py
#     |__ /models.py
#     |__ /tests.py
#     |__ /urls.py
#     |__ /views.py
# |__ /Kumi_judo
#     |__ /asgi.py
#     |__ /settings.py
#     |__ /urls.py
#     |__ /wsgi.py
# |__ /media
# |__ /static
# |__ /templates
#     |__ /calendriers
#         |__ /create_calendrier.html
#         |__ /indexCalendrier.html
#     |__ /classements
#         |__ /create_classement.html
#         |__ /indexClassement.html
#     |__ /judokas
#         |__ /create_judokas.html
#     |__ /base.html
#     |__ /footer.html
#     |__ /header.html
#     |__ /index.html
#     |__ /js.html
#     |__ /message.html
#     |__ /navbar.html
# |__ manage.py


# Créer les applications judokas, calendrier, classement
python manage.py startapp judokas
python manage.py startapp calendrier
python manage.py startapp classement



# ------------------------------------------- Judokas 

# Dans le models.py de judokas
from django.db import models
# Modèle représentant le judokas de judo
class Judokas(models.Model):
    CAT_AGE_CHOICES = [
        ('poussin', 'Poussin(ne)'),
        ('minime', 'Minime'),
        ('cadet', 'Cadet(te)'),
        ('junior', 'Junior'),
        ('senior', 'Senior'),
    ]

    CAT_POIDS_CHOICES = [
        ('-30', '-30 kg'),
        ('-36', '-36 kg'),
        ('-40', '-40 kg'),
        ('-44', '-44 kg'),
        ('-48', '-48 kg'),
        ('-52', '-52 kg'),
        ('-57', '-57 kg'),
        ('-60', '-60 kg'),
        ('-63', '-63 kg'),
        ('-66', '-66 kg'),
        ('-70', '-70 kg'),
        ('-73', '-73 kg'),
        ('-80', '-80 kg'),
        ('-100', '-100 kg'),
        ('+100', '+100 kg'),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    club = models.CharField(max_length=20)
    cat_age = models.CharField(max_length=10, choices=CAT_AGE_CHOICES)
    cat_poids = models.CharField(max_length=10, choices=CAT_POIDS_CHOICES)
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return f"{self.nom} {self.prenom}"


    def get_image_url(self):
        return self.image.url if self.image else None


# Dans forms.py du judokas
from django import forms
from .models import Judokas
# Formulaire basé sur le modèle Judokas
class JudokasForm(forms.ModelForm):
    class Meta:
        model = Judokas
        # Champs du modèle à inclure dans le formulaire
        fields = ['nom', 'prenom', 'club', 'cat_age', 'cat_poids', 'image']

# Dans admin.py:
from django.contrib import admin
# enregistrer les tables
from .models import Judokas

#admin.site.register(Produit) #ce n'est pas encore sous forme de tableau

#Pour qu'il s'affiche en tableau

@admin.register(Judokas) #mettre un decorateur
class JudokasAdmin(admin.ModelAdmin):
    list_display = ('nom' , 'prenom' , 'club' , 'cat_age', 'cat_poids', 'image' )

# Dans apps.py:
from django.apps import AppConfig

# Configuration de l'application "judokas"
class JudokasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'judokas'


# Dans urls.py:
from django.urls import path
from .views import index , CreateJudokas
# Namespace de l'application pour éviter les conflits d'URL
app_name = 'judokas'

# Déclaration des routes de l'application judokas
urlpatterns = [
    path('', index, name='index'),
    path('create-judokas/', CreateJudokas.as_view(), name='create_judokas'),
 
]

# Views.py:

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

# ------------------------------------------- Calendrier
# models.py
from django.db import models
# Modèle représentant un événement de calendrier pour une compétition de judo
class Calendrier(models.Model):
    titre = models.CharField(max_length=200)  # Titre de l'événement
    description = models.TextField()  # Description de l'événement
    date_competiton = models.CharField(max_length=200)  # Date de la compétition (sous forme de texte)
    endroit = models.CharField(max_length=100)  # Lieu de la compétition
    date_publication = models.DateTimeField(auto_now_add=True)  # Date d'enregistrement automatique

    def __str__(self):
        return f"{self.titre}"  # Représentation textuelle d'un objet Calendrier



# admin.py
from django.contrib import admin
from .models import Calendrier

# Enregistre le modèle Calendrier dans l'interface d'administration Django
@admin.register(Calendrier)
class CalendrierAdmin(admin.ModelAdmin):
    # Colonnes à afficher dans la liste des objets Calendrier dans l'admin
    list_display = ('titre', 'description', 'date_competiton', 'endroit', 'date_publication')


# apps.py:
from django.apps import AppConfig
# Configuration de l'application "calendrier"
class CalendrierConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calendrier'

# forms.py
from django import forms
from .models import Calendrier

# Formulaire basé sur le modèle Calendrier
class CalendrierForm(forms.ModelForm):
    class Meta:
        model = Calendrier
        # Champs du modèle à inclure dans le formulaire
        fields = ['titre', 'description', 'date_competiton', 'endroit']


# urls.py
from django.urls import path
from .views import index, CreateCalendrier
# Namespace de l'application pour éviter les conflits d'URL
app_name = 'calendriers'

# Déclaration des routes de l'application calendrier
urlpatterns = [
    path('', index, name='indexCalendrier'),  # Page principale qui liste les calendriers
    path('create-calendrier/', CreateCalendrier.as_view(), name='create_calendrier'),  # Page de création
]

# views.py
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


# ------------------------------------------- Classement

# admin.py
from django.contrib import admin

from .models import Classement
# Enregistre le modèle Classement dans l'interface d'administration Django
@admin.register(Classement)
class ClassementAdmin(admin.ModelAdmin):
    # Colonnes à afficher dans la liste des objets Classement dans l'admin
    list_display = ('judokas','point', 'classements')


# apps.py
from django.apps import AppConfig
# Configuration de l'application "classement"
class ClassementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'classement'



# forms.py
from django import forms
from .models import Classement
# Formulaire basé sur le modèle Classement
class ClassementForm(forms.ModelForm):
    class Meta:
        model = Classement
        # Champs du modèle à inclure dans le formulaire
        fields = ['judokas', 'point', 'classements']



# models.py:
from django.db import models
# Modèle représentant le classement des combattants
class Classement(models.Model):
    judokas = models.ForeignKey('judokas.Judokas', on_delete=models.CASCADE)
    point = models.IntegerField()
    classements = models.IntegerField()

    def __str__(self):
        return f"Classement de {self.judokas.nom}"



# urls.py
from django.urls import path
from .views import index , CreateClassement

# Namespace de l'application pour éviter les conflits d'URL
app_name = 'classements'

# Déclaration des routes de l'application classement
urlpatterns = [
    path('', index, name = 'indexClassement'),
    path('create-classement/', CreateClassement.as_view(), name='create_classement'),

]


# views.py
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

    

# templates/calendriers/create_calendrier.html
{% extends 'base.html' %}
{# Ce template hérite de base.html pour garder la structure commune #}

{% block content %}
{# Début du bloc de contenu principal spécifique à cette page #}

<h1 class="text-center display-3">Ajouter calendrier</h1>

<form method="post" enctype="multipart/form-data">
    {# Formulaire POST pour soumettre les données. enctype est nécessaire si on ajoute des fichiers plus tard #}
    {% csrf_token %}
    {# Protection contre les attaques CSRF (Cross-Site Request Forgery) #}
    
    {{ form.as_p }}
    {# Affiche le formulaire Django en paragraphes #}

   <button type="submit">Ajouter</button>
</form>
{% endblock %}
{# Fin du bloc de contenu #}




# templates/calendriers/indexCalendrier.html
{% extends 'base.html' %}
{# Utilisation de base.html comme layout de base #}

{% block content %}
{# Début du contenu principal #}

<div class="mb-3 text-end">
    <a href="{% url 'calendriers:create_calendrier' %}" class="btn btn-success">Ajouter un calendrier</a>
</div>

<div class="row">
    {# Boucle sur tous les objets calendrier envoyés par la vue #}
    {% for calendrier in calendriers %}
    <div class=""><br><br>
        <div class="card" style="width: 70rem;">
            <div class="card-body">
                <h2 class="card-title">{{ calendrier.titre}}</h2>
                <p class="card-text">{{ calendrier.date_publication}}</p><br>
                <p class="card-text">{{ calendrier.description}}</p>
                <p class="card-text"> Date de compétition : {{ calendrier.date_competiton}}</p>
                <p class="card-text"> Endroit : {{ calendrier.endroit}}</p>
            
            </div>
        </div>
    </div>
    {% endfor %}
    {# Fin de la boucle #}
</div>


{% endblock %}
{# Fin du contenu #}


# templates/classements/create_classement.html
{% extends 'base.html' %}
{# Ce template hérite de base.html pour garder la structure commune #}

{% block content %}
{# Début du bloc de contenu principal spécifique à cette page #}

<h1 class="text-center display-3">Ajouter classement</h1>

<form method="post" enctype="multipart/form-data">
   # Formulaire POST pour soumettre les données. enctype est nécessaire si on ajoute des fichiers plus tard #}
    {% csrf_token %}
    {# Protection contre les attaques CSRF (Cross-Site Request Forgery) #}
    
    {{ form.as_p }}
    {# Affiche le formulaire Django en paragraphes #}

   <button type="submit">Ajouter</button>
</form>
{% endblock %}
{# Fin du bloc de contenu #}



# templates/classements/indexClassement.html
{% extends 'base.html' %}
{# Utilisation de base.html comme layout de base #}

{% block content %}
{# Début du contenu principal #}


<div class="container mt-5">
    <h1 class="text-center display-4 mb-4">Classements</h1>

    <div class="mb-3 text-end">
        <a href="{% url 'classements:create_classement' %}" class="btn btn-success">Ajouter classement</a>
    </div>

    <div class="table-responsive">
        <table class="table table-bordered table-hover align-middle">
            <thead class="table-dark">
                <tr>
                    <th>Judokas</th>
                    <th>Club</th>
                    <th>Cat_age</th>
                    <th>Cat_poids</th>
                    <th>Points</th>
                    <th>Classement</th>
                </tr>
            </thead>
            <tbody>
                {# Boucle sur tous les objets classement envoyés par la vue #}
                {% for classement in classements %}
                <tr>
                    <td>
                        <img src="{{ classement.judokas.image.url }}" alt="Image de {{ classement.judokas.nom }}" width="60" height="60" style="object-fit: cover; border-radius: 50%;">
                        {{ classement.judokas.nom }} {{ classement.judokas.prenom }}
                    </td>                    
                    <td>{{ classement.judokas.club}}</td>
                    <td>{{ classement.judokas.cat_age }}</td>
                    <td>{{ classement.judokas.cat_poids }} kg</td>
                    <td>{{ classement.point }}</td>
                    <td>{{ classement.classements }}</td>
                </tr>
                {% empty %}
                <tr>
                    <td colspan="5" class="text-center text-muted">Aucune commande enregistrée.</td>
                </tr>
                {% endfor %}
                {# Fin de la boucle #}
            </tbody>
        </table>
    </div>
</div>

{% endblock %}
{# Fin du contenu #}

# templates/judokas/create_judokas.html
{% extends 'base.html' %}
{# Ce template hérite de base.html pour garder la structure commune #}

{% block content %}
{# Début du bloc de contenu principal spécifique à cette page #}


<h1 class="text-center display-3">Ajouter Judokas</h1>

<form method="post" enctype="multipart/form-data">
   {# Formulaire POST pour soumettre les données. enctype est nécessaire si on ajoute des fichiers plus tard #}
   {% csrf_token %}
   {# Protection contre les attaques CSRF (Cross-Site Request Forgery) #}
   
   {{ form.as_p }}
   {# Affiche le formulaire Django en paragraphes #}

   <button type="submit">Ajouter</button>
</form>
{% endblock %}
{# Fin du bloc de contenu #}



# dans templates/base.html se trouve la base de l'affichage
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Kumi-judo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4Q6Gf2aSP4eDXB8Miphtr37CMZZQ5oXLH2yaXMJ2w8e2ZtHTl7GptT4jmndRuHDT" crossorigin="anonymous">
  </head>


  <body>
    {% include 'navbar.html' %}
    {% include 'message.html' %}
    <h1></h1>
    <div class="container">
        {% block content %}

        {% endblock %}
    </div>

    {% include 'footer.html' %}
    
  </body>


{% include 'js.html' %}
</html>



# templates/footer.html

<br><br>
<br><br>
<br><br><footer class="bg-light text-center text-lg-start mt-5">
    <div class="container p-4">
      <div class="row">

        <div class="col-lg-4 col-md-6 mb-4 mb-md-0">
          <h5 class="text-success">Fédération Malagasy de Judo</h5>
          <p class="text-muted">
            Promouvoir l'esprit du judo à travers les compétitions, l'entraînement et les valeurs éducatives.
          </p>
        </div>

        <div class="col-lg-4 col-md-6 mb-4 mb-md-0">
          <h5 class="text-success">Liens utiles</h5>
          <ul class="list-unstyled mb-0">
            <li><a href="/" class="text-muted">Judokas</a></li>
            <li><a href="{% url 'classements:indexClassement' %}" class="text-muted">Classements</a></li>
            <li><a href="{% url 'calendriers:indexCalendrier' %}" class="text-muted">Calendrier</a></li>
          </ul>
        </div>
  
        <div class="col-lg-4 col-md-12 mb-4 mb-md-0">
          <h5 class="text-success">Nous suivre</h5>
          <a href="https://web.facebook.com/federationmalagasyjudo" class="me-3 text-primary"><i class="bi bi-facebook"></i> Facebook</a><br>

        </div>
      </div>
    </div>
  
    <div class="text-center p-3 bg-secondary text-white">
      © 2025 Fédération Malagasy de Judo
    </div>

    <!-- Bootstrap Icons (facultatif mais utile pour les icônes) -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">

  </footer>
  

# templates/header.html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Judo</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
        .navbar-judo {
            background-color: #12042e;
        }

        .navbar-judo .nav-link,
        .navbar-judo .navbar-brand {
            color: white;
        }
        

        .navbar-judo .nav-link.active {
            color: #ffd700 !important;
            font-weight: bold;
        }

        .navbar-judo .nav-link.disabled {
            color: #dddddd;
        }

        .btn-primary {
            background-color: #12042e;
            border-color: #12042e;
        }

        .btn-primary:hover {
            background-color: #12042e;
            border-color: #12042e;
            
        }
    </style>
</head>
<body>

<svg class="bi ms-auto d-none" aria-hidden="true"><use href="#check2"></use></svg>

<main class="container">
    <div class="p-5 rounded mt-3" style="background-color:rgb(184, 175, 226); height: 400px;" >
        <h1>Kumi-judo</h1>
        <p class="lead">Bienvenue dans ce site qui permet de voir votre évolution</p>
        <a class="btn btn-lg btn-primary mt-5 " href="../components/navbar" role="button">Calendrier &raquo;</a>
    </div>
</main>



<!-- Bootstrap JS -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>



# templates/index.html
{% extends 'base.html' %}
{# Utilisation de base.html comme layout de base #}

{% block content %}
{# Début du contenu principal #}

<h1 class="text-center display-3">Liste des Judokas</h1>

<div class="mb-3 text-end">
    <a href="{% url 'judokas:create_judokas' %}" class="btn btn-success">Ajouter un judokas</a>
</div>

<div class="row">
    {# Boucle sur tous les objets judokas envoyés par la vue #}
    {% for judoka in judokas %}
    <div class="col-md-4">
        <div class="card" style="width: 18rem;">
            <img src="{{ judoka.get_image_url}}" class="card-img-top" alt="..." style="width: 100%; height: 200px; object-fit: cover">
            <div class="card-body">
                <h5 class="card-title">{{ judoka.nom}} {{ judoka.prenom}}</h5>
                <p class="card-text">{{ judoka.club}}</p>
                <p class="card-text">{{ judoka.cat_age}}</p>
                <p class="card-text">{{ judoka.cat_poids}}</p>

            
            </div>
        </div>
    </div>
    {% endfor %}
</div>


{% endblock %}


# templates/js.html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/js/bootstrap.bundle.min.js" integrity="sha384-j1CDi7MgGQ12Z7Qab0qlWQ/Qqz24Gc6BM0thvEMVjHnfYGF0rmFCozFSxQBxwHKO" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/js/bootstrap.min.js" integrity="sha384-RuyvpeZCxMJCqVUGFI0Do1mQrods/hhxYlcVfGPOfQtPJh0JCw12tUAZ/Mv10S7D" crossorigin="anonymous"></script>


# Pour l'affichage des messages se trouve dans templates/message.html
{% if messages %}

{% for message in messages %}

<div class="alert alert-{{message.tags}} alert-dismissible fade show" role="alert">
    {{ message }}
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>

{% endfor %}
{% endif %}



# Pour le barre de navigation se trouve dans templates/navbar.html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="{% url 'judokas:index' %}">Kumi-judo</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link" aria-current="page" href="/">Judokas</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'classements:indexClassement' %}">Classement</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'calendriers:indexCalendrier' %}">Calendrier</a>
          </li>

        </ul>
        <form class="d-flex" role="search">
          <button class="btn btn-outline-success" type="submit">Se connecter</button>
        </form>
      </div>
    </div>
  </nav>



# Dans manage.py 

#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Kumi_Judo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# Dans settings.py
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / 'templates'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pt4zx#n5@fvs6r_1%ff9&2boyy^hb-8=wx1el10v(qs=npv8$d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'judokas',
    'classement',
    'calendrier',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Kumi_Judo.urls'

# Configuration des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Kumi_Judo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Dossiers pour les fichiers statiques et médias
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Dans kumi_judo/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('judokas.urls')),
    path('classements', include('classement.urls')),
    path('calendriers', include('calendrier.urls')),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)



# Après chaque création du model de chaque application , il faut faire
# Créer les applications judokas, calendrier, classement
# Créer les applications judokas, calendrier, classement
python manage.py makemigrations nom_de_l_application
python manage.py migrate 


# Pour lancer le server
python manage.py runserver
