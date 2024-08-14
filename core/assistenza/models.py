from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.safestring import mark_safe
from django.conf import settings
from flotta.models import Mezzi
from django_utils.choices import Choice, Choices
from django.utils.translation import gettext_lazy as _


def assistenza_directory_path(instance, filename):
    return 'assistenza/azienda_{0}/{1}'.format(instance.descrizione, filename)


class Aziende(models.Model):
    descrizione = models.CharField(max_length=250,help_text='Stabilimento')
    immagine =models.ImageField(upload_to=assistenza_directory_path,default='assistenza/img/assistenza.jpeg', null=True, blank=True,help_text='Caricare un Immagine (opzionale)')
    immagine_thumbnail = ImageSpecField(source='immagine',
                                      processors=[ResizeToFill(40, 40)],
                                      format='JPEG',
                                      options={'quality': 60})
    telefono = PhoneNumberField(blank=True, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    creato = models.DateTimeField(auto_now_add=True)
    aggiornato = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Azienda Assistenza'
        verbose_name_plural = 'Aziende Assistenza'

    def __str__(self):
        return self.descrizione
    
    def get_absolute_url(self):
        return reverse('assistenza:aziende_detail', args=[self.pk])
    
    def get_update_url(self):
        return reverse('assistenza:aziende_update', args=[self.pk])
    
    def get_delete_url(self):
        return reverse('assistenza:aziende_delete', args=[self.pk])
    
    def get_immagine(self):
        if not self.immagine:
            return 'assistenza/img/assistenza.jpeg'
        return self.immagine.url

    def immagine_tag(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % self.get_immagine())
          

class Manutenzione(models.Model):
    operatore = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Operatore', help_text='Operatore')
    id_azienda = models.ForeignKey(Aziende, on_delete=models.CASCADE, verbose_name='Azienda',help_text='Azienda')
    id_mezzo = models.ForeignKey(Mezzi, on_delete=models.CASCADE, verbose_name='Mezzo')
    creato = models.DateTimeField(auto_now_add=True)
    aggiornato = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Interventi(Manutenzione):
    class STATUS(Choices):
       SI = Choice(True, _('SI'))
       NO = Choice(False, _('NO'))

    intervento =  models.TextField(verbose_name='Intervento', help_text='Specificare gli interventi effettuati') 
    ore = models.PositiveIntegerField(verbose_name='Ore',default=0, help_text='Lettura ore di lavoro Mezzo')
    evasa = models.BooleanField(choices=STATUS.choices,default=STATUS.NO)

    class Meta:
        verbose_name = 'Intevento'
        verbose_name_plural = 'Interventi'
        ordering = ["-creato"]

    def __str__(self):
        return f"{self.id_mezzo.descrizione} {self.id_azienda.descrizione}"
    
    def get_absolute_url(self):
        return reverse('assistenza:interventi_detail', args=[self.pk])
    
    def get_update_url(self):
        return reverse('assistenza:interventi_update', args=[self.pk])
    
    def get_delete_url(self):
        return reverse('assistenza:interventi_delete', args=[self.pk])