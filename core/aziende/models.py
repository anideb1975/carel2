from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.safestring import mark_safe


def aziende_directory_path(instance, filename):
    return 'aziende/aziende_{0}/{1}'.format(instance.descrizione, filename)


class Stabilimenti(models.Model):
    descrizione = models.CharField(max_length=250,help_text='Stabilimento')
    immagine =models.ImageField(upload_to=aziende_directory_path,default='aziende/img/aziende.png', null=True, blank=True,help_text='Caricare un Immagine (opzionale)')
    immagine_thumbnail = ImageSpecField(source='immagine',
                                      processors=[ResizeToFill(40, 40)],
                                      format='JPEG',
                                      options={'quality': 60})
    email = models.EmailField(max_length=100, unique=True, blank= True, null=True)
    creato = models.DateTimeField(auto_now_add=True)
    aggiornato = models.DateTimeField(auto_now=True)
    


    class Meta:
        verbose_name = 'Stabilimento'
        verbose_name_plural = 'Stabilimenti'
        
    def get_immagine(self):
        if not self.immagine:
            return '/media/aziende/img/aziende.png'
        return self.immagine.url

    def immagine_tag(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % self.get_immagine())    

    def __str__(self):
        return f"{self.descrizione}"
    
    def get_absolute_url(self):
        return reverse('aziende:stabilimenti_detail', args=[self.pk])
    
    def get_update_url(self):
        return reverse('aziende:stabilimenti_update', args=[self.pk])
    
    def get_delete_url(self):
        return reverse('aziende:stabilimenti_delete', args=[self.pk])


class Ute(models.Model):
    descrizione = models.CharField(max_length=200,help_text='Ute da creare  Es: Ute1')
    id_stabilimento = models.ForeignKey(Stabilimenti, on_delete=models.CASCADE,verbose_name='Stabilimento',help_text='Stabilimento')
    creato = models.DateTimeField(auto_now_add=True)
    aggiornato = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'Ute'
        verbose_name_plural = 'Ute'
    
    def save(self, *args, **kwargs):
        self.descrizione = self.descrizione.upper()
        super().save(*args, **kwargs)    
       

    def __str__(self):
        return f"{self.descrizione} {self.id_stabilimento.descrizione}"
    
    def get_absolute_url(self):
        return reverse('aziende:ute_detail', args=[self.pk])
    
    def get_update_url(self):
        return reverse('aziende:ute_update', args=[self.pk])
    
    def get_delete_url(self):
        return reverse('aziende:ute_delete', args=[self.pk])


class Reparti(models.Model):
    descrizione = models.CharField(max_length=200,help_text='Reparto da creare')
    id_ute = models.ForeignKey(Ute, on_delete=models.CASCADE,verbose_name='Ute')
    creato = models.DateTimeField(auto_now_add=True)
    aggiornato = models.DateTimeField(auto_now=True)
    


    class Meta:
        verbose_name = 'Reparto'
        verbose_name_plural = 'Reparti'
     

    def __str__(self):
        return f"{self.descrizione} {self.id_ute.descrizione} {self.id_ute.id_stabilimento.descrizione}"
    
    def get_absolute_url(self):
        return reverse('aziende:reparti_detail', args=[self.pk])
    
    def get_update_url(self):
        return reverse('aziende:reparti_update', args=[self.pk])
    
    def get_delete_url(self):
        return reverse('aziende:reparti_delete', args=[self.pk])