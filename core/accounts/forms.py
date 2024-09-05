# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import (User,
                     Admin, 
                     Operatore,
                     Responsabile,
                     Assistenza,
                     AssistenzaProfile,
                     UserProfile,
                     )

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,Fieldset,Button, ButtonHolder, HTML
from crispy_forms.bootstrap import InlineRadios 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from betterforms.multiform import MultiModelForm

from .models import (User, Admin, Operatore, Responsabile, Assistenza)

from .models import Squadra

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ['username','squadra','first_name','last_name','avatar']


        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Cognome'}),
           
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password1'].help_text = 'Password'
            self.fields['password1'].widget.attrs = {'placeholder':'Password'}
            self.fields['password2'].help_text = 'Conferma password'
            self.fields['password2'].widget.attrs = {'placeholder':'Conferma Password'}
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
        fields = ['first_name','last_name','squadra','avatar']

class CustomAdminCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Admin
        fields = ['username','squadra','first_name','last_name','avatar']


        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Cognome'}),
           
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['squadra'].choices = Squadra.choices[5:6]
        self.fields['password1'].help_text = 'Password'
        self.fields['password1'].widget.attrs = {'placeholder':'Password'}
        self.fields['password2'].help_text = 'Conferma password'
        self.fields['password2'].widget.attrs = {'placeholder':'Conferma Password'}
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
        fields = ['first_name','last_name','squadra','avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['squadra'].choices = Squadra.choices[5:6]    


class OperatoreCreationForm(UserCreationForm):
    
           
    class Meta:
        model = Operatore
        fields = ['username','squadra','first_name','last_name','avatar']


        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Cognome'}),
           
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['squadra'].choices = Squadra.choices[0:4]
        self.fields['password1'].help_text = 'Password'
        self.fields['password1'].widget.attrs = {'placeholder':'Password'}
        self.fields['password2'].help_text = 'Conferma password'
        self.fields['password2'].widget.attrs = {'placeholder':'Conferma Password'}
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
        fields = ['first_name','last_name','squadra','avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['squadra'].choices = Squadra.choices[0:4]
                

class ResponsabileCreationForm(UserCreationForm):
           
    class Meta:
        model = Responsabile
        fields = ['username','squadra','first_name','last_name']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Cognome'}),
           
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['squadra'].choices = Squadra.choices[0:4]
        self.fields['password1'].help_text = 'Password'
        self.fields['password1'].widget.attrs = {'placeholder':'Password'}
        self.fields['password2'].help_text = 'Conferma password'
        self.fields['password2'].widget.attrs = {'placeholder':'Conferma Password'}
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
        fields = ['first_name','last_name','squadra','avatar']        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['squadra'].choices = Squadra.choices[0:4]


class AssistenzaCreationForm(UserCreationForm):
           
    class Meta:
        model = Assistenza
        fields = ['username','first_name','last_name','squadra']


        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Cognome'}),
           
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['squadra'].choices = Squadra.choices[4:5]
        self.fields['password1'].help_text = 'Password'
        self.fields['password1'].widget.attrs = {'placeholder':'Password'}
        self.fields['password2'].help_text = 'Conferma password'
        self.fields['password2'].widget.attrs = {'placeholder':'Conferma Password'}
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


class AssistenzaChangeForm(UserChangeForm):
    password = None
    
    class Meta:
        model = Assistenza
        fields = ['first_name','last_name','squadra','avatar'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['squadra'].choices = Squadra.choices[4:5]

class AssistenzaProfiliForm(forms.ModelForm):
    class Meta:
        model = AssistenzaProfile
        fields  = ['azienda'] 

class UserProfiliForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields  = ('azienda',)


class AssistenzaCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': AssistenzaCreationForm,
        'profile': AssistenzaProfiliForm,
    }

class UserCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': CustomUserCreationForm,
        'profile': UserProfiliForm,
    }

class AdminCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': CustomAdminCreationForm,
        'profile': UserProfiliForm,
    }

class OperatoreCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': OperatoreCreationForm,
        'profile': UserProfiliForm,
    }

class ResponsabileCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': ResponsabileCreationForm,
        'profile': UserProfiliForm,
    }


class UserEditMultiForm(MultiModelForm):
    form_classes = {
        'user': UserChangeForm,
        'profile': UserProfiliForm,
    }

class AdminEditMultiForm(MultiModelForm):
    form_classes = {
        'user': CustomAdminChangeForm,
        'profile': UserProfiliForm,
    }

class OperatoreEditMultiForm(MultiModelForm):
    form_classes = {
        'user': OperatoreChangeForm,
        'profile': UserProfiliForm,
    }

class ResponsabileEditMultiForm(MultiModelForm):
    form_classes = {
        'user': ResponsabileChangeForm,
        'profile': UserProfiliForm,
    }

class AssistenzaEditMultiForm(MultiModelForm):
    form_classes = {
        'user': AssistenzaChangeForm,
        'profile': AssistenzaProfiliForm,
    }

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