from django.urls import path
from .views import index , CreateClassement

# Namespace de l'application pour éviter les conflits d'URL
app_name = 'classements'

# Déclaration des routes de l'application classement
urlpatterns = [
    path('', index, name = 'indexClassement'),
    path('create-classement/', CreateClassement.as_view(), name='create_classement'),

]