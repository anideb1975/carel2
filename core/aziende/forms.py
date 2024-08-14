from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,Fieldset,Button, ButtonHolder, HTML

from .models import (Stabilimenti, Ute, Reparti)

class StabilimentiForm(forms.ModelForm):
    
    class Meta:
        model = Stabilimenti
        fields = ['descrizione','immagine','email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
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
                                    HTML('<a class="btn btn-warning" href={%  url "aziende:stabilimenti_list" %}>Cancel</a>'),
                                    css_class='form-row py-4'
                                ),
                            )       
        )        
     )

class UteForm(forms.ModelForm):
    
    class Meta:
        model = Ute
        fields = ['descrizione','id_stabilimento']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('descrizione', css_class='form-group col-md-4 mb-0'),
                Column('id_stabilimento', css_class='form-group col-md-4 mb-0'),
                css_class='form-row '
            ),
            Row (
                            Column(
                                ButtonHolder(
                                    Submit('Save', 'Save', css_class='btn btn-primary rounded-1'),
                                    HTML('<a class="btn btn-warning" href={%  url "aziende:ute_list" %}>Cancel</a>'),
                                    css_class='form-row py-4'
                                ),
                            )       
        )        
     )

class RepartiForm(forms.ModelForm):
    
    class Meta:
        model = Reparti
        fields = ['id_ute','descrizione']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('descrizione', css_class='form-group col-md-4 mb-0'),
                Column('id_ute', css_class='form-group col-md-4 mb-0'),
                css_class='form-row '
            ),
            Row (
                            Column(
                                ButtonHolder(
                                    Submit('Save', 'Save', css_class='btn btn-primary rounded-1'),
                                    HTML('<a class="btn btn-warning" href={%  url "aziende:reparti_list" %}>Cancel</a>'),
                                    css_class='form-row py-4'
                                ),
                            )       
        )        
     )                    