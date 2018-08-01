from django.db import models



# Create your models here.


class Text(models.Model):
    slowo = models.CharField(max_length=1000)


    def __str__(self):
        return self.slowo

class Author(models.Model):
    imie = models.CharField(max_length=200)

    def __str__(self):
        return self.imie

class Stats(models.Model):
    slowo = models.CharField(max_length=20)
    liczebnosc = models.IntegerField()

    def __str__(self):
        return self.slowo




