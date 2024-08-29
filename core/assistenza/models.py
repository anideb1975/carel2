from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.safestring import mark_safe
from django.conf import settings
from flotta.models import Mezzi
from checklist.models import Controlli
from django_utils.choices import Choice, Choices
from django.utils.translation import gettext_lazy as _
from aziende.models import Stabilimenti

def assistenza_directory_path(instance, filename):
    return 'assistenza/azienda_{0}/{1}'.format(instance.descrizione, filename)


class Aziende(models.Model):
    descrizione = models.CharField("Azienda Assistenza",max_length=250,help_text='Azienda che fornisce assistenza e manutenzione',unique=True)
    immagine =models.ImageField(upload_to=assistenza_directory_path,default='/static/assistenza/img/assistenza.jpeg', null=True, blank=True,help_text='Caricare un Immagine (opzionale)')
    immagine_thumbnail = ImageSpecField(source='immagine',
                                      processors=[ResizeToFill(40, 40)],
                                      format='JPEG',
                                      options={'quality': 60})
    id_stabilimento = models.ManyToManyField(Stabilimenti, verbose_name='Stabilimenti Serviti')
    email = models.EmailField(max_length=100, unique=True)
    creato = models.DateTimeField(auto_now_add=True)
    aggiornato = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Azienda Assistenza'
        verbose_name_plural = 'Aziende Assistenza'

    # Salvo campo email lettere minuscole
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)    

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
            return '/static/assistenza/img/assistenza.jpeg'
        return self.immagine.url

    def immagine_tag(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % self.get_immagine())
          


class Interventi(models.Model):
    class STATUS(Choices):
       SI = Choice(True, _('Si'))
       NO = Choice(False, _('Salva e riprendi più tardi'))
       
    operatore = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Operatore', help_text='Operatore')
    modificato = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='operatore',verbose_name='Operatore', help_text='Operatore')
    id_controllo = models.ForeignKey(Controlli, on_delete=models.CASCADE, verbose_name='Controllo')
    intervento =  models.TextField(verbose_name='Intervento', help_text='Specificare gli interventi effettuati') 
    ore = models.PositiveIntegerField(verbose_name='Ore',default=0, help_text='Lettura ore di lavoro Mezzo')
    evasa = models.BooleanField(choices=STATUS.choices,default=STATUS.NO)
    creato = models.DateTimeField(auto_now_add=True)
    aggiornato = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'Intevento'
        verbose_name_plural = 'Interventi'
        ordering = ["-creato"]

    def __str__(self):
        return f"{self.id_controllo}"
    
    def get_absolute_url(self):
        return reverse('assistenza:interventi_detail', args=[self.pk])
    
    def get_update_url(self):
        return reverse('assistenza:interventi_update', args=[self.pk])
    
    def get_delete_url(self):
        return reverse('assistenza:interventi_delete', args=[self.pk])

    