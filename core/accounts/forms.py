# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import (User,
                     Admin, 
                     Operatore,
                     Responsabile,
                     Assistenza,
                     )

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,Fieldset,Button, ButtonHolder, HTML
from crispy_forms.bootstrap import InlineRadios 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import (User, Operatore, Responsabile, Assistenza)

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ['username','squadra','first_name','last_name','avatar']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Row(
                    Column('username', css_class='form-group col-md-6 mb-0'),
                    Column('squadra', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row '
                ),
            
                Row(
                    Column('first_name', css_class='form-group col-md-6 mb-0'),
                    Column('last_name', css_class='form-group col-md-6 mb-0'),
                    
                    css_class='form-row'
                ),

                Row(
                    Column('password1', css_class='form-group col-md-6 mb-0'),
                    Column('password2', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                
                Row (
                    Column(
                        ButtonHolder(
                            Submit('Save', 'Registrati', css_class='btn btn-gray-800'),
                            css_class='d-grid'
                        ),
            )        
        )
    )        

class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name','last_name','avatar']

class CustomAdminCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Admin
        fields = ['username','squadra','first_name','last_name','avatar']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Row(
                    Column('username', css_class='form-group col-md-6 mb-0'),
                    Column('squadra', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row '
                ),
            
                Row(
                    Column('first_name', css_class='form-group col-md-6 mb-0'),
                    Column('last_name', css_class='form-group col-md-6 mb-0'),
                    
                    css_class='form-row'
                ),

                Row(
                    Column('password1', css_class='form-group col-md-6 mb-0'),
                    Column('password2', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                
                Row (
                    Column(
                        ButtonHolder(
                            Submit('Save', 'Registrati', css_class='btn btn-gray-800'),
                            css_class='d-grid'
                        ),
            )        
        )
    )        

class CustomAdminChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = Admin
        fields = ['first_name','last_name','avatar']


class OperatoreCreationForm(UserCreationForm):
           
    class Meta:
        model = Operatore
        fields = ['username','squadra','first_name','last_name','avatar']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                Column('squadra', css_class='form-group col-md-6 mb-0'),
                css_class='form-row '
            ),
           
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                
                css_class='form-row'
            ),

             Row(
                Column('password1', css_class='form-group col-md-6 mb-0'),
                Column('password2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
             
            Row (
                Column(
                    ButtonHolder(
                        Submit('Save', 'Registrati', css_class='btn btn-gray-800'),
                        css_class='d-grid'
                    ),
        )        
    )
)        
        
        
class OperatoreChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = Operatore
        fields = ['squadra','first_name','last_name','avatar']
                

class ResponsabileCreationForm(UserCreationForm):
           
    class Meta:
        model = Responsabile
        fields = ['username','squadra','first_name','last_name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                Column('squadra', css_class='form-group col-md-6 mb-0'),
                css_class='form-row '
            ),
           
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

             Row(
                Column('password1', css_class='form-group col-6 mb-0'),
                Column('password2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row (
                Column(
                    ButtonHolder(
                        Submit('Save', 'Registrati', css_class='btn btn-gray-800'),
                       css_class='d-grid'
                    ),
        )        
    )
)            
        

class ResponsabileChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = Responsabile
        fields = ['squadra','first_name','last_name','avatar']        



class AssistenzaCreationForm(UserCreationForm):
           
    class Meta:
        model = Assistenza
        fields = ['username','first_name','last_name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                css_class='form-row '
            ),
           
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

             Row(
                Column('password1', css_class='form-group col-6 mb-0'),
                Column('password2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row (
                Column(
                    ButtonHolder(
                        Submit('Save', 'Registrati', css_class='btn btn-gray-800'),
                       css_class='d-grid'
                    ),
        )        
    )
)            


class AssistenzaChangeForm(UserChangeForm):
    password = None
    
    class Meta:
        model = Assistenza
        fields = ['first_name','last_name','avatar'] 


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())


""" # Sezione Form Profili

class OperatoreProfiliForm(forms.ModelForm):
    class Meta:
        model = OperatoreProfile
        fields  = ['user','badge','squadra','avatar']

class ResponsabileProfiliForm(forms.ModelForm):
    class Meta:
        model = ResponsabileProfile
        fields  = ['user','badge','squadra','avatar']   

class ManutenzioneProfiliForm(forms.ModelForm):
    class Meta:
        model = ManutenzioneProfile
        fields  = ['user','avatar']                 """