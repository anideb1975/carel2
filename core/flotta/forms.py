from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,Fieldset,Button, ButtonHolder, HTML
from .models import (Categorie,Mezzi)

class CategorieForm(forms.ModelForm):
    
    class Meta:
        model = Categorie
        fields = ['descrizione','immagine','id_reparto']

        widgets = {
            "id_reparto": forms.Select(attrs={'id': 'reparto', 'required': 'required'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('id_reparto', css_class='form-group col-md-6 mb-0'),
                Column('descrizione', css_class='form-group col-md-6 mb-0'),
                css_class='form-row '
            ),
             Row(
                Column('immagine', css_class='form-group col-md-8 mb-0'),
                css_class='form-row '
            ),
            Row (
                            Column(
                                ButtonHolder(
                                    Submit('Save', 'Save', css_class='btn btn-primary rounded-1'),
                                    HTML('<a class="btn btn-warning" href={%  url "flotta:categorie_list" %}>Cancel</a>'),
                                    css_class='form-row py-4'
                                ),
                            )       
        )        
    )


class MezziForm(forms.ModelForm):
    
    class Meta:
        model = Mezzi
        fields = ['id_categoria','interno','descrizione','immagine','matricola']

        widgets = {
            "id_categoria": forms.Select(attrs={'id': 'reparto', 'required': 'required'}),

        }    
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('id_categoria', css_class='form-group col-md-6 mb-0'),
                Column('interno', css_class='form-group col-md-6 mb-0'),
                css_class='form-row '
            ),
            Row(
                Column('descrizione', css_class='form-group col-md-6 mb-0'),
                Column('matricola', css_class='form-group col-md-6 mb-0'),
                css_class='form-row '
                
            ),
             Row(
                Column('immagine', css_class='form-group col-md-8 mb-0'),
                css_class='form-row '
                
            ),
            Row (
                            Column(
                                ButtonHolder(
                                    Submit('Save', 'Save', css_class='btn btn-primary rounded-1'),
                                    HTML('<a class="btn btn-warning" href={%  url "flotta:mezzi_list" %}>Cancel</a>'),
                                    css_class='form-row py-4'
                                ),
                            )       
        )        
    )    
        
        
              