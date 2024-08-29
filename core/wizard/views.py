from .forms import (StabilimentoWizard,
                    UteWizard,
                    RepartiWizard,
                    CategorieWizard,
                    MezziWizard,
                    AssistenzaWizard,
                    )
from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
import os

from assistenza.models import Aziende


class CarelWizard(LoginRequiredMixin,UserPassesTestMixin,SessionWizardView):
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'photos'))
    template_name = 'wizard/wizard.html'
    form_list = [StabilimentoWizard,UteWizard,RepartiWizard,CategorieWizard,MezziWizard,AssistenzaWizard]


    def test_func(self):
        return  self.request.user.is_superuser or self.request.user.role == "ADMIN"

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('home')

    def done(self, form_list, **kwargs):
        stabilimento_form = form_list[0]
        stabilimento = stabilimento_form.save(commit=False)
        stabilimento.save()
        ute_form = form_list[1]
        ute = ute_form.save(commit=False)
        ute.id_stabilimento = stabilimento
        ute.save()
        reparto_form = form_list[2]
        reparto = reparto_form.save(commit=False)
        reparto.id_ute = ute
        reparto.save()
        categoria_form = form_list[3]
        categoria = categoria_form.save(commit=False)
        categoria.id_reparto = reparto
        categoria.save()
        mezzo_form = form_list[4]
        mezzo = mezzo_form.save(commit=False)
        mezzo.id_categoria = categoria
        mezzo.save()
        assistenza_form = form_list[5]
        assistenza = assistenza_form.save(commit=False)
        assistenza.save()
        assistenza.id_stabilimento.add(stabilimento)
        assistenza.save()
        
        
        return render(self.request, 'wizard/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })



