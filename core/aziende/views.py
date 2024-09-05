from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,DetailView
from django.contrib.auth.mixins import  LoginRequiredMixin,UserPassesTestMixin
from .forms import (StabilimentiForm, UteForm, RepartiForm)
from .models import (Stabilimenti, Ute, Reparti)

from view_breadcrumbs import (DetailBreadcrumbMixin, 
                              ListBreadcrumbMixin, 
                              DeleteBreadcrumbMixin, 
                              CreateBreadcrumbMixin,
                              UpdateBreadcrumbMixin,
)

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin   

from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory,NamedFormsetsMixin


### Inline Ute ###

class UteInlineView(InlineFormSetFactory):
    model = Ute
    form_class = UteForm
    #formset_class = BaseItemFormSet
    #initial = [{'name': 'example1'}, {'name', 'example2'}]
    #prefix = 'item-form'
    prefix = 'form'
    factory_kwargs = {'extra': 2, 'max_num': 10,
                      'can_order': False, 'can_delete': True}
    #formset_kwargs = {'auto_id': 'my_id_%s'}


### Fine ###
autocomplete='off'

### Crud Aziende ###

class AziendeViewCreate(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,CreateBreadcrumbMixin,NamedFormsetsMixin,CreateWithInlinesView):
    form_class = StabilimentiForm
    model = Stabilimenti
    inlines = [UteInlineView]
    template_name = "aziende/stabilimenti/create.html"
    success_url = reverse_lazy('aziende:stabilimenti_list')
    success_message = "Created successfully"

    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('aziende:stabilimenti_list')
    
    def get_context_data(self, **kwargs):
        context = super(AziendeViewCreate, self).get_context_data(**kwargs)
        context["titolo"] = "Crea Stabilimento"
        return context


class AziendeViewUpdate(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,UpdateBreadcrumbMixin,UpdateWithInlinesView):
    form_class = StabilimentiForm
    model = Stabilimenti
    inlines = [UteInlineView]
    success_url = reverse_lazy('aziende:stabilimenti_list')
    template_name = 'aziende/stabilimenti/update.html'
    success_message = "Update successfully"

    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('aziende:stabilimenti_list')
    
    def get_context_data(self, **kwargs):
        context = super(AziendeViewUpdate, self).get_context_data(**kwargs)
        context["titolo"] = "Aggiorna Stabilimenti"
        return context 
    
    

    
class AziendeViewList(LoginRequiredMixin,ListBreadcrumbMixin,ListView):
    model = Stabilimenti
    template_name = 'aziende/stabilimenti/list.html'
    
    def get_context_data(self, **kwargs):
        context = super(AziendeViewList, self).get_context_data(**kwargs)
        context["titolo"] = "Stabilimenti"
        context['segment'] = 'page-'
        return context   

class AziendeViewDelete(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,DeleteBreadcrumbMixin,DeleteView):
    model = Stabilimenti
    success_url = reverse_lazy('aziende:stabilimenti_list')
    template_name = 'aziende/stabilimenti/delete.html'
    success_message = "Delete successfully"

    
    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('aziende:stabilimenti_list')
    
    def get_context_data(self, **kwargs):
        context = super(AziendeViewDelete, self).get_context_data(**kwargs)
        context["titolo"] = "Cancella Aziende"
        return context 

class AziendeViewDetail(LoginRequiredMixin,DetailBreadcrumbMixin, DetailView):
    model = Stabilimenti
    success_url = reverse_lazy('aziende:stabilimenti_list')
    template_name = 'aziende/stabilimenti/detail.html'

    
    def get_context_data(self, **kwargs):
        context = super(AziendeViewDetail, self).get_context_data(**kwargs)
        context["titolo"] = "Dettagli Aziende"
        return context 

### Fine crud Aziende ###          


## Crud Ute ####


### Inline Reparti ###

class RepartiInlineView(InlineFormSetFactory):
    model = Reparti
    form_class = RepartiForm
    #formset_class = BaseItemFormSet
    #initial = [{'name': 'example1'}, {'name', 'example2'}]
    #prefix = 'item-form'
    factory_kwargs = {'extra': 1, 'max_num': 10, 'can_order': False, 'can_delete': True}
    #formset_kwargs = {'auto_id': 'my_id_%s'}

### Fine ###


class UteViewCreate(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,CreateBreadcrumbMixin,CreateWithInlinesView):
    form_class = UteForm
    model = Ute
    inlines = [RepartiInlineView]
    template_name = 'aziende/ute/create.html'
    success_url = reverse_lazy('aziende:ute_list')
    success_message = "Created successfully"

    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('aziende:ute_list')
    
    def get_context_data(self, **kwargs):
        context = super(UteViewCreate, self).get_context_data(**kwargs)
        context["titolo"] = "Crea Ute"
        return context


class UteViewUpdate(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,UpdateBreadcrumbMixin,UpdateWithInlinesView):
    form_class = UteForm
    model = Ute
    inlines = [RepartiInlineView]
    success_url = reverse_lazy('aziende:ute_list')
    template_name = 'aziende/ute/update.html'
    success_message = "Update successfully"

    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('aziende:ute_list')
    
    def get_context_data(self, **kwargs):
        context = super(UteViewUpdate, self).get_context_data(**kwargs)
        context["titolo"] = "Aggiorna Ute"
        return context


class UteViewList(LoginRequiredMixin,ListBreadcrumbMixin,ListView):
    model = Ute
    template_name = 'aziende/ute/list.html'

    
    def get_context_data(self, **kwargs):
        context = super(UteViewList, self).get_context_data(**kwargs)
        context["titolo"] = "Ute"
        context['segment'] = 'page-'
        return context   

class UteViewDelete(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin, DeleteBreadcrumbMixin, DeleteView):
    model = Ute
    success_url = reverse_lazy('aziende:ute_list')
    template_name = 'aziende/ute/delete.html'
    success_message = "Delete successfully"
    
    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('aziende:ute_list')
    
    def get_context_data(self, **kwargs):
        context = super(UteViewDelete, self).get_context_data(**kwargs)
        context["titolo"] = "Cancella Ute"
        return context       

class UteViewDetail(LoginRequiredMixin, DetailBreadcrumbMixin, DetailView):
    model = Ute
    success_url = reverse_lazy('aziende:ute_list')
    template_name = 'aziende/ute/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(UteViewDetail, self).get_context_data(**kwargs)
        context["titolo"] = "Dettagli Ute"
        return context       

### Fine Crud Ute ###


### Crud Reparti  ###

class RepartiViewCreate(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin, CreateBreadcrumbMixin, CreateView):
    form_class = RepartiForm
    model = Reparti
    success_url = reverse_lazy('aziende:reparti_list')
    template_name = 'aziende/reparti/create.html'
    success_message = "Created successfully"
    
    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('aziende:reparti_list')
    
    def get_context_data(self, **kwargs):
        context = super(RepartiViewCreate, self).get_context_data(**kwargs)
        context["titolo"] = "Crea Reparti"
        return context

class RepartiViewUpdate(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,UpdateBreadcrumbMixin, UpdateView):
    form_class = RepartiForm
    model  = Reparti
    success_url = reverse_lazy('aziende:reparti_list')
    template_name = 'aziende/reparti/update.html'
    success_message = "Update successfully"

    
    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('aziende:reparti_list')
    
    def get_context_data(self, **kwargs):
        context = super(RepartiViewUpdate, self).get_context_data(**kwargs)
        context["titolo"] = "Aggiorna Reparto"
        return context    
    
class RepartiViewList(LoginRequiredMixin,ListBreadcrumbMixin, ListView):
    model = Reparti
    template_name = 'aziende/reparti/list.html'
    
    def get_context_data(self, **kwargs):
        context = super(RepartiViewList, self).get_context_data(**kwargs)
        context["titolo"] = "Reparti"
        context['segment'] = 'page-'
        return context   

class RepartiViewDelete(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,DeleteBreadcrumbMixin, DeleteView):
    model = Reparti
    success_url = reverse_lazy('aziende:reparti_list')
    template_name = 'aziende/reparti/delete.html'
    success_message = "Delete successfully"
    
    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('aziende:reparti_list')
    
    def get_context_data(self, **kwargs):
        context = super(RepartiViewDelete, self).get_context_data(**kwargs)
        context["titolo"] = "Cancella Reparto"
        return context       

class RepartiViewDetail(LoginRequiredMixin, DetailBreadcrumbMixin, DetailView):
    model = Reparti
    template_name = 'aziende/reparti/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(RepartiViewDetail, self).get_context_data(**kwargs)
        context["titolo"] = "Dettagli Reparto"
        return context      

### Fine crud Reparti
