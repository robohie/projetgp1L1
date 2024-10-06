from django.db import models


# Create your models here.
class Teachers(models.Model):
    nom = models.CharField(max_length=20)
    postnom = models.CharField(max_length=20)
    promo = models.CharField(max_length=5)
    point = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignants"

    def __str__(self):
        return ' '.join((self.nom, self.postnom, str(self.point)))
