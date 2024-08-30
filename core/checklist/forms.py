from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, ButtonHolder, HTML
from crispy_forms.bootstrap import InlineRadios 

from .models import CheckList, Controlli

class CheckListForm(forms.ModelForm):
    
    class Meta:
        model = CheckList
        fields  = '__all__'
        exclude = ['operatore']
       

class ControlliForm(forms.ModelForm):

    class Meta:
        model = Controlli
        fields = '__all__'
        exclude = ['id_checklist']
    
        widgets = {
            'controllo_luci_lampeggiante': forms.RadioSelect(),
            'controllo_avvisatori': forms.RadioSelect,
            'controllo_sollevamento': forms.RadioSelect,
            'controllo_telaio': forms.RadioSelect,
            'controllo_batteria': forms.RadioSelect,
            'controllo_forche': forms.RadioSelect,
            'sostituzione_batteria': forms.RadioSelect,
            'anomalie': forms.Textarea(attrs={'rows': 8}),
            "id_mezzo":forms.Select(attrs={'id':'mezzi','required':'required'}),

        }    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
           
                    Row(
                        Column('anomalie', css_class='form-control row-4 mb-0'),
                    ),
               
   )    
        

class AnomalieControlliForm(forms.ModelForm):
    
    class Meta:
        model = Controlli
        fields  = ['anomalie']
        
        widgets = {
            'anomalie': forms.Textarea(attrs={'rows': 3}),

        }    
