from django.contrib import admin
from .models import Controlli,CheckList
from .forms import ControlliForm

class ControlliInline(admin.StackedInline):
    model = Controlli
    extra = 1
    max_num = 1
    form = ControlliForm

    

class CheckListAdmin(admin.ModelAdmin):
    list_display = ['operatore','turno','creato','aggiornato']
    list_filter = ['operatore','turno','creato','aggiornato']
    inlines = [ControlliInline]

    
class ControlliAdmin(admin.ModelAdmin):
    list_display = ['id_checklist','id_mezzo']
    list_filter = ['id_checklist','id_mezzo']
    form = ControlliForm
   
    
    

admin.site.register(Controlli, ControlliAdmin)
admin.site.register(CheckList,CheckListAdmin)

