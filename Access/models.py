from django.db import models


# Create your models here.
class Student(models.Model):
    nom = models.CharField(max_length=20)
    postnom = models.CharField(max_length=20)
    matricule = models.CharField(max_length=15, unique=True)
    state = models.IntegerField(max_length=1, default=0, verbose_name="état")
    promo = models.CharField(max_length=5)

    class Meta:
        verbose_name = "Etudiant"
        verbose_name_plural = "Etudiants"

    def __str__(self):
        return ' '.join((self.nom, self.postnom, self.promo))
