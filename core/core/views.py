from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.base import TemplateView
import sweetify
from aziende.models import Stabilimenti
from accounts.models import User
from assistenza.models import Aziende
from view_breadcrumbs import BaseBreadcrumbMixin


msg1 = """
    Sembra che non ci siano dati al momento,
    per iniziare a usare l'applicazione devi popolare il database
    con dei dati, puoi usare il tasto WIZARD presente nella tua SIDEBAR per velocizzare
    la procedura (CONSIGLIATO).
    ATTENZIONE (se non popoli il databese non potrai registrare nuovi utenti)
"""

msg2 = """
    Oppure chiudere questo messaggio e popolare il
    database manualmente utilizzando le sezioni che sono presenti
    nella sidebar. 
"""

class HomeView(BaseBreadcrumbMixin,TemplateView):
    template_name = 'home.html'
    crumbs = [("Home Page", reverse_lazy("home"))]

    def get (self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect("index") 
        return super().get( request, *args, **kwargs)
    
    def get_template_names(self):
        stabilimenti = Stabilimenti.objects.all().exists()
        assistenza = Aziende.objects.all().exists()
        if not stabilimenti or not assistenza:
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
        context['utenti'] = User.objects.filter(is_superuser=True).exists()
        context['stabilimenti'] = Stabilimenti.objects.all().exists()
        context ['assistenza'] = Aziende.objects.all().exists()
        return context
    


def permission_denied(request, exception=None, template_name='403.html'):
    return render(request, '403.html')


def not_found(request, exception=None, template_name='404.html'):
    return render(request, '404.html')


def server_error(request, exception=None, template_name='500.html'):
    return render(request, '500.html')
