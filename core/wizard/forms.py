from django import forms
from aziende.models import (Stabilimenti,Ute,Reparti)
from assistenza.models import Aziende
from flotta.models import (Categorie, Mezzi)
from phonenumber_field.formfields import PhoneNumberField

class StabilimentoWizard(forms.ModelForm):
    
    class Meta:
        model = Stabilimenti
        fields = ('descrizione',)

        widgets = {
            'descrizione': forms.TextInput(attrs={'placeholder': 'Stabilimento'}),
        }

class UteWizard(forms.ModelForm):
    
    class Meta:
        model = Ute
        fields =  ('descrizione',)

        widgets = {
            'descrizione': forms.TextInput(attrs={'placeholder': 'Ute'}),
        }

class RepartiWizard(forms.ModelForm):
    
    class Meta:
        model = Reparti
        fields = ('descrizione',)

        widgets = {
            'descrizione': forms.TextInput(attrs={'placeholder': 'Reparto'}),
        }                

class CategorieWizard(forms.ModelForm):
    
    class Meta:
        model = Categorie
        fields = ('descrizione','immagine',)

        widgets = {
            'descrizione': forms.TextInput(attrs={'placeholder': 'Categoria Mezzi'}),
        }  

class MezziWizard(forms.ModelForm):
    
    class Meta:
        model = Mezzi
        fields = ('interno','descrizione','matricola',)

        widgets = {
            'interno': forms.TextInput(attrs={'placeholder': 'Interno'}),
            'descrizione': forms.TextInput(attrs={'placeholder': 'Descrizione'}),
            'matricola': forms.TextInput(attrs={'placeholder': 'Matricola'}),
        }         

class AssistenzaWizard(forms.ModelForm):
    #telefono = PhoneNumberField(region="IT"),
    
    class Meta:
        model = Aziende
        fields =  ('descrizione','telefono','email')

        widgets = {
            'descrizione': forms.TextInput(attrs={'placeholder': 'Azienda Assistenza'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }