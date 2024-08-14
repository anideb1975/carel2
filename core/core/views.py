from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.base import TemplateView



class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['utente'] =  self.request.user    
        return context
