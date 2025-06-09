from django.urls import path
from .views import index, CreateCalendrier

# Namespace de l'application pour éviter les conflits d'URL
app_name = 'calendriers'

# Déclaration des routes de l'application calendrier
urlpatterns = [
    path('', index, name='indexCalendrier'),  # Page principale qui liste les calendriers
    path('create-calendrier/', CreateCalendrier.as_view(), name='create_calendrier'),  # Page de création
]
