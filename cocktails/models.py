from django.db import models

__all__=[
    "Cocktail",
]

# Create your models here.
class cocktail(models.Model):
    nome = models.CharField(max_length=200)
    descrizione = models.TextField()
    immagine = models.ImageField(upload_to='cocktails')

class PuntoVendita(models.Model):
    nome = models.CharField(max_length=200)
    indirizzo = models.CharField(max_length=1024)
    telefono = models.CharField(max_length=20)
    capienza = models.IntegerField(blank=True, null = True)
    è_un_bar = models.BooleanField(default=False)

    def __str__(self):
        return(
            f"{seld.nome}"
            f"({"bar" if seld.self.è_un_bar else "ristorante"})"
        )
