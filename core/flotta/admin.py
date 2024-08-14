from django.contrib import admin
from .models import (Categorie, Mezzi)


class MezziInLine(admin.TabularInline):
    model = Mezzi
    
class CategoriaAdmin(admin.ModelAdmin):
    model = Categorie
    inlines = [MezziInLine]
    list_display = ['descrizione','id_reparto']
    admin_order = 1   

class MezziAdmin(admin.ModelAdmin):
    model = Mezzi
    list_display = ['interno','descrizione','matricola', 'id_categoria','creato','aggiornato']
    admin_order = 2     

admin.site.register(Categorie,CategoriaAdmin)
admin.site.register(Mezzi,MezziAdmin)