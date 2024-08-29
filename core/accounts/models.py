# users/models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from assistenza.models import Aziende
from aziende.models import Stabilimenti


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'accounts/avatar_{0}/{1}'.format(instance.username, filename)


class Squadra(models.IntegerChoices):
        SQUADRA_A =  1, "SQUADRA A"
        SQUADRA_B =  2, "SQUADRA B"
        SQUADRA_C =  3, "SQUADRA C"
        BITURNISTA =  4, "BITURNISTA"
        ASSISTENZA =  5, "ASSISTENZA"
        ADMIN = 6,"ADMIN"

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "ADMIN"
        OPERATORE = "OPERATORE", "OPERATORE"
        RESPONSABILE = "RESPONSABILE", "RESPONSABILE"
        ASSISTENZA = "ASSISTENZA", "ASSISTENZA"
        
    base_role = Role.ADMIN
    first_name = models.CharField(max_length=100, verbose_name='Nome')
    last_name= models.CharField(max_length=100,verbose_name='Cognome')
    squadra = models.PositiveSmallIntegerField(choices=Squadra.choices,verbose_name='Squadra',default=Squadra.ADMIN)
    role = models.CharField(max_length=50, choices=Role.choices,verbose_name='Ruolo')
    avatar = models.ImageField(upload_to=user_directory_path ,default='/static/img/operatore/operatore.png', null=True, blank=True)
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(40, 40)],
                                      format='JPEG',
                                      options={'quality': 60})
    last_login = models.DateTimeField(default=timezone.now,verbose_name='Ultimo Accesso')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creato')
    updated = models.DateTimeField(auto_now=True, verbose_name='Aggiornato')
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name']


    def get_avatar(self):
        if not self.avatar:
            return '/static/avatar/img/operatore/operatore.png'
        return self.avatar.url

    def avatar_tag(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % self.get_avatar())
   
    
    avatar_tag.short_description = 'Avatar'
    
    
    def __str__(self):
        return str(self.username)
    
    
    def save(self, *args, **kwargs):
        if not self.pk or self.role == None:
            self.role = self.base_role    
        return super().save(*args, **kwargs)

    


class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ADMIN)

class Admin(User):

    base_role = User.Role.ADMIN
    base_squadra = Squadra.ADMIN

    objects = AdminManager()

    class Meta:
        proxy = True
        verbose_name = 'Admin'
        verbose_name_plural = 'Admin'
        
    def save(self, *args, **kwargs):
        if not self.pk or self.role == None:
            self.role = self.base_role
        self.squadra = self.base_squadra
        return super().save(*args, **kwargs)    



    
class OperatoreManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.OPERATORE)


class Operatore(User):

    base_role = User.Role.OPERATORE

    objects = OperatoreManager()

    class Meta:
        proxy = True
        verbose_name = 'Operatore'
        verbose_name_plural = 'Operatori'
        
    def save(self, *args, **kwargs):
        if not self.pk or self.role == None:
            self.role = self.base_role
        return super().save(*args, **kwargs)    

class ResponsabileManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.RESPONSABILE)


class Responsabile(User):

    base_role = User.Role.RESPONSABILE

    objects = ResponsabileManager()

    class Meta:
        proxy = True
        verbose_name = 'Responsabile'
        verbose_name_plural = 'Responsabili'
        
        
    def save(self, *args, **kwargs):
        if not self.pk or self.role == None:
            self.role = self.base_role
        return super().save(*args, **kwargs)            


class AssistenzaManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ASSISTENZA)


class Assistenza(User):

    base_role = User.Role.ASSISTENZA
    base_squadra = Squadra.ASSISTENZA

    objects = AssistenzaManager()

    class Meta:
        proxy = True
        verbose_name = 'Assistenza'
        verbose_name_plural = 'Assistenza'
        
    def save(self, *args, **kwargs):
        if not self.pk or self.role == None:
            self.role = self.base_role
        self.squadra = self.base_squadra    
        return super().save(*args, **kwargs)    

class AssistenzaProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Operatore Manutenzione')
    azienda = models.ForeignKey(Aziende, on_delete=models.CASCADE, null=True,verbose_name='Azienda')
    
    class Meta:
        verbose_name = 'Profilo Operatore Manutenzione'
        verbose_name_plural = 'Profilo Operatore Manutenzione'
    
    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Operatore')
    azienda = models.ForeignKey(Stabilimenti, on_delete=models.CASCADE, null=True,verbose_name='Stabilimento')
    
    class Meta:
        verbose_name = 'Profilo Utente'
        verbose_name_plural = 'Profili Utenti'
    
    def __str__(self):
        return self.user.username        
    

""" class OperatoreProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    badge = models.CharField(max_length=50, unique=True,verbose_name='Badge')
    squadra = models.PositiveSmallIntegerField(choices=Squadra.choices,default=Squadra.SQUADRA_A,verbose_name='Squadra')
    avatar = models.ImageField(upload_to=user_directory_path ,default='avatar/img/operatore/operatore.png', null=True, blank=True)
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(40, 40)],
                                      format='JPEG',
                                      options={'quality': 60})
    
    class Meta:
        verbose_name = 'Profilo Operatore'
        verbose_name_plural = 'Profilo Operatori'
        
    def __str__(self):
        return self.user.username    
    
    
    def get_avatar(self):
        if not self.avatar:
            return '/media/avatar/img/operatore/operatore.png'
        return self.avatar.url

    def avatar_tag(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % self.get_avatar())
   
    
    avatar_tag.short_description = 'Avatar'

@receiver(post_save, sender=Operatore)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "OPERATORE":
        OperatoreProfile.objects.create(user=instance)
    
    
class ResponsabileProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    badge = models.CharField(max_length=50, unique=True,verbose_name='Badge')
    squadra = models.PositiveSmallIntegerField(choices=Squadra.choices,default=Squadra.SQUADRA_A,verbose_name='Squadra')
    avatar = models.ImageField(upload_to=user_directory_path ,default='avatar/img/responsabile/responsabile.png', null=True, blank=True)
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(40, 40)],
                                      format='JPEG',
                                      options={'quality': 60})
    
    class Meta:
        verbose_name = 'Profilo Responsabile'
        verbose_name_plural = 'Profilo Responsabili'
    
    def __str__(self):
        return self.user.username    
    
    def get_avatar(self):
        if not self.avatar:
            return '/media/avatar/img/responsabile/responsabile.png'
        return self.avatar.url

    def avatar_tag(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % self.get_avatar())
   
    
    avatar_tag.short_description = 'Avatar'


@receiver(post_save, sender=Responsabile)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "RESPONSABILE":
        ResponsabileProfile.objects.create(user=instance)
 
 
class ManutenzioneProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Operatore Manutenzione')
    avatar = models.ImageField(upload_to=user_directory_path ,default='avatar/img/manutenzione/manutenzione.jpg', null=True, blank=True)
    id_azienda = models.ForeignKey(Aziende, on_delete=models.CASCADE, null=True,verbose_name='Azienda')
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(40, 40)],
                                      format='JPEG',
                                      options={'quality': 60})
    
    class Meta:
        verbose_name = 'Profilo Operatore Manutenzione'
        verbose_name_plural = 'Profilo Operatore Manutenzione'
    
    def __str__(self):
        return self.user.username    
    
    def get_avatar(self):
        if not self.avatar:
            return 'avatar/img/manutenzione/manutenzione.jpg'
        return self.avatar.url

    def avatar_tag(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % self.get_avatar())
   
    
    avatar_tag.short_description = 'Avatar'


@receiver(post_save, sender=Manutenzione)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "MANUTENZIONE":
        ManutenzioneProfile.objects.create(user=instance)                   """