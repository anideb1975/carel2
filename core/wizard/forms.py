from django import forms
from aziende.models import (Stabilimenti,Ute,Reparti)
from assistenza.models import Aziende
from flotta.models import (Categorie, Mezzi)


class StabilimentoWizard(forms.ModelForm):
    
    class Meta:
        model = Stabilimenti
        fields = ('descrizione','immagine','email')

        widgets = {
            'descrizione': forms.TextInput(attrs={'placeholder': 'Stabilimento'}),
        }

        labels = {
            "descrizione": "Stabilimento",
            
        }

class UteWizard(forms.ModelForm):
    
    class Meta:
        model = Ute
        fields =  ('descrizione',)

        widgets = {
            'descrizione': forms.TextInput(attrs={'placeholder': 'Ute'}),
        }

        labels = {
            "descrizione": "Ute di Stabilimento",
            
        }

class RepartiWizard(forms.ModelForm):
    
    class Meta:
        model = Reparti
        fields = ('descrizione',)

        widgets = {
            'descrizione': forms.TextInput(attrs={'placeholder': 'Reparto'}),
        }                

        labels = {
            "descrizione": "Reparto",
            
        }

class CategorieWizard(forms.ModelForm):
    
    class Meta:
        model = Categorie
        fields = ('descrizione','immagine',)

        widgets = {
            'descrizione': forms.TextInput(attrs={'placeholder': 'Categoria Mezzi'}),
        }

        labels = {
            "descrizione": "Categorie di Mezzi",
            
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
        labels = {
            "descrizione": "Descrizone del Mezzo",
            "interno": "Identificativo univoco del Mezzo",
            "matricola": "Matricola del Mezzo"
            
        }         

class AssistenzaWizard(forms.ModelForm):
    
    class Meta:
        model = Aziende
        fields =  ('id','descrizione','email',)

        widgets = {
            'descrizione': forms.TextInput(attrs={'placeholder': 'Azienda Assistenza'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }


