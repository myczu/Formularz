from django.contrib import admin
from .models import Venue
# Register your models here.

class VenueAdmin(admin.ModelAdmin):
    list_display = ['id', 'imie', 'nazwisko', 'data_wyjazdu', 'godzina_wyjazdu', 'dlugosc_trasy']


admin.site.register(Venue, VenueAdmin)