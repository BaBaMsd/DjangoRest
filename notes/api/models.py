from django.db import models
#from django.contrib.gis.db import models
# Create your models here.

class Notes(models.Model):
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

    class Meta:
        ordering = ['-updated']

class Baba(models.Model):
    nom = models.CharField(max_length=50)
    loc = models.CharField(max_length=400)
