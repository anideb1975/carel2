from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse

from flotta.models import  Mezzi
from django_utils.choices import Choice, Choices
User  = get_user_model()


CONTROLLI = [ 'CONTROLLO LUCI LAMPEGGIANTE',
              'CONTROLLO AVVISATORI ACUSTICI (MANUALE E RETROMARCIA)',
              'CONTROLLO DISPOSITIVO SOLLEVAMENTO STERZO',
              'ANOMALIE TELAIO (PORTE, VETRI, ecc.)',
              'CONTROLLO FUNZIONALE BATTERIA (CARICA) RABOCCHI (SE NECESSARIO)',
              'CONTROLLO PRESENZA BLOCCO SICUREZZA USCITA FORCHE',
              'LA SOSTITUZIONE DELLA BATTERIA VIENE VISUALIZZATO SUL DISPLAY CIRCA 20%',
            ]

class CheckList(models.Model):
    class Turni(models.TextChoices):
        PRIMO = 'PRIMO', _('Primo')
        SECONDO = 'SECONDO', _('Secondo')
        TERZO = 'TERZO', _('Terzo')
        CENTRALE = 'CENTRALE',_('Centrale')
        
    operatore = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Operatore')
    turno = models.CharField(max_length=100,choices=Turni.choices,default=Turni.PRIMO)
    #id_stabilimento = models.ForeignKey(Stabilimenti, on_delete=models.CASCADE,verbose_name='Stabilimento')
    #id_ute = ChainedForeignKey(Ute,chained_field="id_stabilimento",auto_choose=True, chained_model_field="id_stabilimento", on_delete=models.CASCADE,verbose_name='Ute')
    #id_reparto = ChainedForeignKey(Reparti, chained_field="id_ute", auto_choose=True,chained_model_field="id_ute", on_delete=models.CASCADE,verbose_name='Reparto')
    #id_categoria = ChainedForeignKey(Categorie,chained_field="id_reparto", auto_choose=True, chained_model_field="id_reparto" ,on_delete=models.CASCADE,verbose_name='Categoria')
    #id_mezzo = ChainedForeignKey(Mezzi,chained_field="id_categoria", auto_choose=True, chained_model_field="id_categoria" ,on_delete=models.CASCADE,verbose_name='Mezzo')
    creato = models.DateTimeField(auto_now_add=True)
    aggiornato = models.DateTimeField(auto_now=True) 
    
    class Meta:
        verbose_name = 'Checklist'
        verbose_name_plural = 'Checklists'
        ordering = ["-creato"]     
    
    def __str__(self):
        return f"{self.operatore.username}"
    
    def get_absolute_url(self):
        return reverse('checklist:checklist_detail', args=[self.pk])
    
    def get_update_url(self):
        return reverse('checklist:checklist_update', args=[self.pk])
    
    def get_delete_url(self):
        return reverse('checklist:checklist_delete', args=[self.pk])
    

class Controlli(models.Model):
    class STATUS(Choices):
        OK = Choice('OK', _('OK'))
        KO = Choice('KO', _('KO'))
        
    
    id_checklist = models.ForeignKey(CheckList, on_delete=models.CASCADE,verbose_name='CheckList')
    id_mezzo = models.ForeignKey(Mezzi, on_delete=models.CASCADE, verbose_name='Mezzo')
    controllo_luci_lampeggiante = models.CharField('Controllo luci lampeggiante',max_length=2, choices=STATUS.choices,default=STATUS.OK,help_text=CONTROLLI[0])
    controllo_avvisatori = models.CharField('Controllo avvisatori',max_length=2,choices=STATUS.choices,default=STATUS.OK,help_text=CONTROLLI[1])
    controllo_sollevamento = models.CharField('Controllo sollevamento',max_length=2,choices=STATUS.choices,default=STATUS.OK,help_text=CONTROLLI[2])
    controllo_telaio = models.CharField('Controllo telaio',max_length=2,choices=STATUS.choices,default=STATUS.OK,help_text=CONTROLLI[3])
    controllo_batteria = models.CharField('Controllo batteria',max_length=2,choices=STATUS.choices,default=STATUS.OK,help_text=CONTROLLI[4])
    controllo_forche = models.CharField('Controllo forche',max_length=2,choices=STATUS.choices,default=STATUS.OK,help_text=CONTROLLI[5])
    sostituzione_batteria = models.CharField('Sostituzione Batteria',max_length=2,choices=STATUS.choices,default=STATUS.OK,help_text=CONTROLLI[6])
    anomalie = models.TextField(null=True, blank = True)
    
    class Meta:
        verbose_name = 'Controllo'
        verbose_name_plural = 'Controlli'
        
        
    def __str__(self):
      return f"{self.id_checklist}"
  
    def get_absolute_url(self):
        return reverse('checklist:controlli_detail', args=[self.pk])
    
    def get_update_url(self):
        return reverse('checklist:controlli_update', args=[self.pk])
    
    def get_delete_url(self):
        return reverse('checklist:controlli_delete', args=[self.pk])
    
    def get_fields_and_values(self):
        return [(field.name.replace("_"," "), field.value_to_string(self)) for field in Controlli._meta.fields if field.name not in ['id','id_checklist','id_mezzo','controlli_ptr','anomalie'] ]

    def get_num_controlli(self):
        value = 0
        values = self.get_fields_and_values()
        for fld, val in values:
            value = value +1 
        return value

    def get_ok(self):
        value = 0
        values = self.get_fields_and_values()
        for fld, val in values:
            if val == "OK":
                value = value +1 
        return value
    
    def get_ko(self):
        value = 0
        values = self.get_fields_and_values()
        for fld, val in values:
            if val == "KO":
                value = value +1 
        return value          

    def percentuale_ok(self):
        return int(self.get_ok() * 100 / self.get_num_controlli())   
    
    def percentuale_ko(self):
        return int(self.get_ko() * 100 / self.get_num_controlli())
           