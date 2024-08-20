from django.db import models
from aziende.models import Reparti
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.safestring import mark_safe

def categoria_directory_path(instance, filename):
    return 'categorie/categorie_{0}/{1}'.format(instance.descrizione, filename)

def mezzi_directory_path(instance, filename):
    return 'mezzi/mezzi_{0}/{1}'.format(instance.descrizione, filename)



class Categorie(models.Model):
    descrizione = models.CharField(max_length=100, verbose_name='Descrizione',help_text='Inserire la Categoria di Mezzi')
    id_reparto = models.ForeignKey(Reparti, on_delete=models.CASCADE,verbose_name='Reparto',help_text='Reparto')
    immagine =models.ImageField(upload_to=categoria_directory_path ,default='categoria/img/categorie.jpeg', null=True, blank=True,help_text='Caricare un Immagine (opzionale)')
    immagine_thumbnail = ImageSpecField(source='immagine',
                                      processors=[ResizeToFill(40, 40)],
                                      format='JPEG',
                                      options={'quality': 60})
    creato = models.DateTimeField(auto_now_add=True)
    aggiornato = models.DateTimeField(auto_now=True)
    
        
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorie'

    def get_immagine(self):
        if not self.immagine:
            return '/media/categoria/img/categorie.jpeg'
        return self.immagine.url

    def immagine_tag(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % self.get_immagine())    
    
    def __str__(self):
        return f"{self.descrizione} {self.id_reparto}"
    
    def get_absolute_url(self):
        return reverse('flotta:categorie_detail', args=[self.pk])
    
    def get_update_url(self):
        return reverse('flotta:categorie_update', args=[self.pk])
    
    def get_delete_url(self):
        return reverse('flotta:categorie_delete', args=[self.pk])


class Mezzi(models.Model):
    interno = models.CharField(max_length=5, verbose_name='Interno del Mezzo',help_text='Inserire un Identificativo univoco, Es. CR1',unique=True)
    descrizione  = models.CharField(max_length=100,verbose_name='Descrizione',help_text='Descrizione del Mezzo')
    matricola   = models.CharField(max_length=20, unique=True,verbose_name='Matricola Mezzo',help_text='Inserire numero matricola ( presente sul mezzo)')
    immagine =models.ImageField(upload_to=mezzi_directory_path ,default='mezzi/img/carrello.jpg', null=True, blank=True,help_text='Caricare un Immagine (opzionale)')
    immagine_thumbnail = ImageSpecField(source='immagine',
                                      processors=[ResizeToFill(40, 40)],
                                      format='JPEG',
                                      options={'quality': 60})
    id_categoria = models.ForeignKey(Categorie, on_delete=models.CASCADE,verbose_name='Categoria')
    creato = models.DateTimeField(auto_now_add=True)
    aggiornato = models.DateTimeField(auto_now=True)
    
    # Salvo campo interno lettere maiuscole
    def save(self, *args, **kwargs):
        self.interno = self.interno.upper()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Mezzo'
        verbose_name_plural = 'Mezzi'

    def get_immagine(self):
        if not self.immagine:
            return '/media/mezzi/img/carrello.jpg'
        return self.immagine.url

    def immagine_tag(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % self.get_immagine())    
        
    def __str__(self):
        return f"{self.interno} {self.id_categoria.descrizione} {self.id_categoria.id_reparto.descrizione} {self.id_categoria.id_reparto.id_ute}"     
    
    def get_absolute_url(self):
        return reverse('flotta:mezzi_detail', args=[self.pk])
    
    def get_update_url(self):
        return reverse('flotta:mezzi_update', args=[self.pk])
    
    def get_delete_url(self):
        return reverse('flotta:mezzi_delete', args=[self.pk])     


