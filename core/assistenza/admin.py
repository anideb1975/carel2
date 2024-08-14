from django.contrib import admin
from .models import (Aziende,
                     Interventi,
                     )


class AziendeAdmin(admin.ModelAdmin):
    readonly_fields = ['immagine_tag']
    list_display = ['immagine_tag','descrizione','telefono','email']
    list_display_links = ['descrizione','immagine_tag']



class InterventiAdmin(admin.ModelAdmin):
    list_display = ['operatore','id_azienda','id_mezzo','ore','evasa','creato','aggiornato']         

admin.site.register(Aziende,AziendeAdmin)
admin.site.register(Interventi,InterventiAdmin)

