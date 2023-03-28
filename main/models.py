from django.db import models

class Venue(models.Model):
    imie = models.CharField('imie', max_length=50)
    nazwisko = models.CharField('nazwisko', max_length=50)
    poczatkowy_stan_licznika = models.IntegerField('poczatkowy stan licznika')
    godzina_wyjazdu = models.CharField('godzina wyjazdu', max_length=50)
    data_wyjazdu = models.CharField('data wyjazdu', max_length=50)
    trasa = models.CharField('trasa', max_length=50)
    koncowy_stan_licznika = models.IntegerField('koncowy stan licznika')
    uwagi_kierowcy = models.CharField('uwagi', max_length=50)
    dlugosc_trasy = models.IntegerField('dlugosc trasy')

    def __str__(self):
        return self.imie
