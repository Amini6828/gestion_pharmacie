from django.db import models

# Create your models here.

class article(models.Model):
    titre= models.CharField(max_length=200)
    contenu= models.TextField(200)
    auteur= models.CharField(max_length=100)
    date_creation= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre