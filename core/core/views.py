from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.base import TemplateView
import sweetify
from aziende.models import Stabilimenti
from accounts.models import User



msg1 = """
    Sembra che non ci siano dati al momento,
    per iniziare a usare l'applicazione devi popolare il database
    con dei dati, puoi usare il tasto WIZARD presente nella tua SIDEBAR per velocizzare
    la procedura (CONSIGLIATO).
"""

msg2 = """
    Oppure chiudere questo messaggio e popolare il
    database manualmente utilizzando le sezioni che sono presenti
    nella sidebar. 
"""

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'
    
    def get_template_names(self):
        stabilimenti = Stabilimenti.objects.all()
        if not stabilimenti:
            args1 = dict(title='Info1', icon='info', text= msg1 , persistent="Next")
            args2 = dict(title='Info2', icon='info', text=msg2,  persistent="Close")
            sweetify.multiple(self.request, args1, args2)
        else:
            return super().get_template_names()
    
        return super().get_template_names()
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['utente'] =  self.request.user    
        return context


class RegistratiView(TemplateView):
    template_name = 'registrati.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['utenti'] = User.objects.get(role='ADMIN') 
        return context