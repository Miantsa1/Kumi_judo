from django.urls import path
from .views import index , CreateJudokas

# Namespace de l'application pour éviter les conflits d'URL
app_name = 'judokas'

# Déclaration des routes de l'application judokas
urlpatterns = [
    path('', index, name='index'),
    path('create-judokas/', CreateJudokas.as_view(), name='create_judokas'),

    
]