from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,DetailView
from django.contrib.auth.mixins import  LoginRequiredMixin,UserPassesTestMixin
from .forms import (AziendeForm,
                    InterventiForm,
                    )
from .models import (Aziende,
                     Interventi,
                     )


from view_breadcrumbs import (DetailBreadcrumbMixin, 
                              ListBreadcrumbMixin, 
                              DeleteBreadcrumbMixin, 
                              CreateBreadcrumbMixin,
                              UpdateBreadcrumbMixin,
                              BaseBreadcrumbMixin,
)

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from flotta.models import (Mezzi)

from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
import datetime


### Crud Aziende ###

class AziendeViewCreate(LoginRequiredMixin,UserPassesTestMixin,CreateBreadcrumbMixin,CreateView):
    form_class = AziendeForm
    model = Aziende
    success_url = reverse_lazy('assistenza:aziende_list')
    template_name = 'assistenza/aziende/create.html'
    
    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser 

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('assistenza:aziende_list')
    
    
    def get_context_data(self, **kwargs):
        context = super(AziendeViewCreate, self).get_context_data(**kwargs)
        context["titolo"] = "Aziende Assistenza"
        return context

class AziendeViewUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateBreadcrumbMixin,UpdateView):
    form_class = AziendeForm
    model = Aziende
    success_url = reverse_lazy('assistenza:aziende_list')
    template_name = 'assistenza/aziende/update.html'
    
    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request ,"Not Authorized")
        return redirect('assistenza:aziende_list')
    
    def get_context_data(self, **kwargs):
        context = super(AziendeViewUpdate, self).get_context_data(**kwargs)
        context["titolo"] = "Aggiorna Aziende Assistenza"
        return context    
    
class AziendeViewList(LoginRequiredMixin,ListBreadcrumbMixin,ListView):
    model = Aziende
    template_name = 'assistenza/aziende/list.html'
    
    def get_context_data(self, **kwargs):
        context = super(AziendeViewList, self).get_context_data(**kwargs)
        context["titolo"] = "Assistenza"
        context['segment'] = 'assistenza'
        return context   

class AziendeViewDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteBreadcrumbMixin,DeleteView):
    model = Aziende
    success_url = reverse_lazy('assistenza:aziende_list')
    template_name = 'assistenza/aziende/delete.html'

    
    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('assistenza:aziende_list')
    
    def get_context_data(self, **kwargs):
        context = super(AziendeViewDelete, self).get_context_data(**kwargs)
        context["titolo"] = "Cancella Aziende"
        return context 

class AziendeViewDetail(LoginRequiredMixin,DetailBreadcrumbMixin, DetailView):
    model = Aziende
    success_url = reverse_lazy('assistenza:aziende_list')
    template_name = 'assistenza/aziende/detail.html'

    
    def get_context_data(self, **kwargs):
        context = super(AziendeViewDetail, self).get_context_data(**kwargs)
        context["titolo"] = "Dettagli Aziende Assistenza"
        return context 

### Fine crud Aziende ###          

#### Sezione Interventi ####

class InterventiCreateView(SuccessMessageMixin, UserPassesTestMixin,BaseBreadcrumbMixin, LoginRequiredMixin,CreateView):
    model = Interventi
    form_class = InterventiForm
    template_name = 'assistenza/interventi/create.html'
    success_url = reverse_lazy('assistenza:interventi_list')  # Sostituisci con la tua URL di successo
    success_message = "Created successfully"
    crumbs = [("Crea Interventi", reverse_lazy("assistenza:interventi_create"))]

    def test_func(self):
        return  self.request.user.role == 'ASSISTENZA' or self.request.user.is_superuser or self.request.role == "ADMIN"

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('assistenza:interventi_list')


    def get_context_data(self, **kwargs):
        context = super(InterventiCreateView, self).get_context_data(**kwargs)
        context["titolo"] = "Intervento"
        context['mezzo'] = Mezzi.objects.get(pk=self.kwargs.get('pk'))
        return context 
    
    def form_valid(self, form, **kwargs):
        form.instance.id_mezzo = Mezzi.objects.get(pk=self.kwargs.get('pk'))
        form.instance.operatore = self.request.user
        return super().form_valid(form)    
    

class InterventiViewList(LoginRequiredMixin,ListBreadcrumbMixin,ListView):
    model = Interventi
    template_name = "assistenza/interventi/list.html"
    
    def get_context_data(self, **kwargs):
        context = super(InterventiViewList, self).get_context_data(**kwargs)
        context["titolo"] = "Interventi"
        context['segment'] = 'assistenza'
        return context      

class InterventiViewDetail(LoginRequiredMixin, DetailBreadcrumbMixin, DetailView):
    model = Interventi
    template_name = "assistenza/interventi/detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(InterventiViewDetail, self).get_context_data(**kwargs)
        context["titolo"] = "Dettagli Interventi."
        return context 

class InterventiUpdateView(SuccessMessageMixin,UserPassesTestMixin,LoginRequiredMixin,UpdateBreadcrumbMixin,UpdateView):
    model = Interventi
    form_class = InterventiForm
    template_name = "assistenza/interventi/update.html"
    #success_url = reverse_lazy('assistenza:interventi_list')
    success_message = "Update successfully"

    def get_success_url(self):
        return reverse_lazy('assistenza:interventi_detail', kwargs={'pk': self.object.pk})
    
    def test_func(self):
        return self.get_object().operatore == self.request.user or self.request.user.role == 'ADMIN'  or self.request.user.is_superuser  or  self.request.user.role == 'ASSISTENZA'

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('assistenza:interventi_list')

    
    def get_context_data(self, **kwargs):
        context = super(InterventiUpdateView, self).get_context_data(**kwargs)
        context["titolo"] = "Update Interventi"
        return context

class InterventiViewDelete(LoginRequiredMixin, UserPassesTestMixin,DeleteBreadcrumbMixin, DeleteView):
    model = Interventi
    success_url = reverse_lazy('assistenza:interventi_list')
    success_message = "Delete successfully"
    template_name = "assistenza/interventi/delete.html"

    def test_func(self):
        return self.get_object().operatore == self.request.user or self.request.user.role == 'ADMIN' or self.request.user.is_superuser 

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('assistenza:interventi_list')  

    
    def get_context_data(self, **kwargs):
        context = super(InterventiViewDelete, self).get_context_data(**kwargs)
        context["titolo"] = "Delete"
        return context       


#### fine sezione Interventi ####