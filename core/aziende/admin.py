from django.contrib import admin
from .models import (Stabilimenti, Reparti, Ute)


class RepartiInline(admin.TabularInline):
    model = Reparti


class UteInline(admin.TabularInline):
    model = Ute
    
    
    
class StabilimentiAdmin(admin.ModelAdmin):
    model = Stabilimenti
    readonly_fields = ['immagine_tag']
    list_display = ['immagine_tag','descrizione','email']
    list_display_links = ['immagine_tag','descrizione']
    inlines = [UteInline]
    admin_order = 1
   
    
    
class UteAdmin(admin.ModelAdmin):
    model = Ute
    list_display = ['descrizione','id_stabilimento']
    inlines = [RepartiInline]
    admin_order = 2
  

class RepartiAdmin(admin.ModelAdmin):
    model = Reparti
    list_display = ['descrizione','id_ute']
    admin_order = 3     


admin.site.register(Stabilimenti,StabilimentiAdmin)
admin.site.register(Ute,UteAdmin)
admin.site.register(Reparti,RepartiAdmin)

