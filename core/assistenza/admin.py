from django.contrib import admin
from .models import (Aziende,
                     Interventi,
                     )


class AziendeAdmin(admin.ModelAdmin):
    readonly_fields = ['immagine_tag']
    list_display = ['immagine_tag','descrizione','email']
    list_display_links = ['descrizione','immagine_tag']
    filter_horizontal = ['id_stabilimento']



class InterventiAdmin(admin.ModelAdmin):
    list_display = ['operatore','id_controllo','ore','evasa','creato','aggiornato']         

admin.site.register(Aziende,AziendeAdmin)
admin.site.register(Interventi,InterventiAdmin)

