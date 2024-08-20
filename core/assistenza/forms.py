from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,Fieldset,Button, ButtonHolder, HTML
from .models import (Aziende,
                     Interventi,
                     )

class AziendeForm(forms.ModelForm):
    
    class Meta:
        model = Aziende
        fields = '__all__'


class InterventiForm(forms.ModelForm):


    class Meta:
        model = Interventi
        fields = ['intervento','ore','evasa']  # Non includere ' id_controllo', perché lo stai impostando nella view   

        widgets = {
            'intervento': forms.Textarea(attrs={'rows': 8}),
            'evasa': forms.RadioSelect(),
        } 

class UpdateInterventiForm(forms.ModelForm):


    class Meta:
        model = Interventi
        fields = ['intervento','ore','evasa']  # Non includere ' id_controllo', perché lo stai impostando nella view   

        widgets = {
            #"id_azienda":forms.Select(attrs={'id':'azienda','required':'required'}),
            'intervento': forms.Textarea(attrs={'rows': 6}),
            'evasa': forms.RadioSelect(),
        } 

    