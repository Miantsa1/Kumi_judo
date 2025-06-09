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

