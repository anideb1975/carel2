from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,DetailView
from django.contrib.auth.mixins import  LoginRequiredMixin,UserPassesTestMixin
from .forms import (CategorieForm,MezziForm)
from .models import (Categorie, Mezzi)


from view_breadcrumbs import (DetailBreadcrumbMixin, 
                              ListBreadcrumbMixin, 
                              DeleteBreadcrumbMixin, 
                              CreateBreadcrumbMixin,
                              UpdateBreadcrumbMixin,
)

from django.contrib import messages   
from django.contrib.messages.views import SuccessMessageMixin  
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory


### Inline Ute ###

class MezziInlineView(InlineFormSetFactory):
    model = Mezzi
    form_class = MezziForm
    #formset_class = BaseItemFormSet
    #initial = [{'name': 'example1'}, {'name', 'example2'}]
    #prefix = 'item-form'
    factory_kwargs = {'extra': 1, 'max_num': None,
                      'can_order': False, 'can_delete': True}
    #formset_kwargs = {'auto_id': 'my_id_%s'}


### Fine ###


### Crud Categorie  ###

class CategorieViewCreate(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,CreateBreadcrumbMixin,CreateWithInlinesView):
    form_class = CategorieForm
    model = Categorie
    success_url = reverse_lazy('flotta:categorie_list')
    template_name = 'flotta/categorie/create.html'
    success_message = "Created successfully"
    inlines = [MezziInlineView]

    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('flotta:categorie_list')
    
    
    def get_context_data(self, **kwargs):
        context = super(CategorieViewCreate, self).get_context_data(**kwargs)
        context["titolo"] = "Categorie"
        return context


class CategorieViewUpdate(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,UpdateBreadcrumbMixin,UpdateWithInlinesView):
    form_class = CategorieForm
    model = Categorie
    success_url = reverse_lazy('flotta:categorie_list')
    template_name = 'flotta/categorie/update.html'
    success_message = "Created successfully"
    inlines = [MezziInlineView]


    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('flotta:categorie_list')
    
    def get_context_data(self, **kwargs):
        context = super(CategorieViewUpdate, self).get_context_data(**kwargs)
        context["titolo"] = "Aggiorna Categorie"
        return context 


class CategorieViewList(LoginRequiredMixin,ListBreadcrumbMixin,ListView):
    model = Categorie
    template_name = 'flotta/categorie/list.html'
    
    def get_context_data(self, **kwargs):
        context = super(CategorieViewList, self).get_context_data(**kwargs)
        context["titolo"] = "Categorie"
        context['segment'] = 'tables-bootstrap-'
        return context    

class CategorieViewDelete(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,DeleteBreadcrumbMixin, DeleteView):
    model = Categorie
    success_url = reverse_lazy('flotta:categorie_list')
    template_name = 'flotta/categorie/delete.html'
    success_message = "Delete successfully"

    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('flotta:categorie_list')
    
    def get_context_data(self, **kwargs):
        context = super(CategorieViewDelete, self).get_context_data(**kwargs)
        context["titolo"] = "Cancella Categorie"
        return context 

class CategorieViewDetail(LoginRequiredMixin, DetailBreadcrumbMixin, DetailView):
    model = Categorie
    template_name = 'flotta/categorie/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(CategorieViewDetail, self).get_context_data(**kwargs)
        context["titolo"] = "Dettagli Categorie"
        return context 

### Fine crud categorie  ###          


## Crud Mezzi ####

class MezziViewCreate(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,CreateBreadcrumbMixin, CreateView):
    form_class = MezziForm
    model  = Mezzi
    success_url = reverse_lazy('flotta:mezzi_list')
    template_name = 'flotta/mezzi/create.html'
    success_message = "Created successfully"
    
    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('flotta:mezzi_list')
    
    def get_context_data(self, **kwargs):
        context = super(MezziViewCreate, self).get_context_data(**kwargs)
        context["titolo"] = "Mezzi"
        return context

class MezziViewUpdate(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin, UpdateBreadcrumbMixin, UpdateView):
    form_class = MezziForm
    model = Mezzi
    success_url = reverse_lazy('flotta:mezzi_list')
    template_name = 'flotta/mezzi/update.html'
    success_message = "Update successfully"
    
    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('flotta:mezzi_list')
    
    def get_context_data(self, **kwargs):
        context = super(MezziViewUpdate, self).get_context_data(**kwargs)
        context["titolo"] = "Aggiorna Mezzi"
        return context    
    
class MezziViewList(LoginRequiredMixin, ListBreadcrumbMixin, ListView):
    model = Mezzi
    app_name = 'flotta'
    template_name = 'flotta/mezzi/list.html'
    
    def get_context_data(self, **kwargs):
        context = super(MezziViewList, self).get_context_data(**kwargs)
        context["titolo"] = "Mezzi"
        context['segment'] = 'tables-bootstrap-'
        return context   

class MezziViewDelete(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,DeleteBreadcrumbMixin, DeleteView):
    model = Mezzi
    success_url = reverse_lazy('flotta:mezzi_list')
    template_name = 'flotta/mezzi/delete.html'
    success_message = "Delete successfully"
    
    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('flotta:mezzi_list')
    
    def get_context_data(self, **kwargs):
        context = super(MezziViewDelete, self).get_context_data(**kwargs)
        context["titolo"] = "Cancella Mezzi"
        return context       

class MezziViewDetail(LoginRequiredMixin, DetailBreadcrumbMixin,DetailView):
    model = Mezzi
    success_url = reverse_lazy('flotta:mezzi_list')
    template_name = 'flotta/mezzi/detail.html'

    
    def get_context_data(self, **kwargs):
        context = super(MezziViewDetail, self).get_context_data(**kwargs)
        context["titolo"] = "Dettagli Mezzi"
        return context       

### Fine Crud Mezzi ###


""" 
class CategorieViewCreate(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,CreateBreadcrumbMixin,CreateView):
    form_class = CategorieForm
    model = Categorie
    success_url = reverse_lazy('flotta:categorie_list')
    template_name = 'flotta/categorie/create.html'
    success_message = "Created successfully"
    
    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('flotta:categorie_list')
    
    
    def get_context_data(self, **kwargs):
        context = super(CategorieViewCreate, self).get_context_data(**kwargs)
        context["titolo"] = "Categorie"
        return context

class CategorieViewUpdate(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,UpdateBreadcrumbMixin,UpdateView):
    form_class = CategorieForm
    model = Categorie
    success_url = reverse_lazy('flotta:categorie_list')
    template_name = 'flotta/categorie/update.html'
    success_message = "Update successfully"
    
    def test_func(self):
        return  self.request.user.role == 'ADMIN' or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('flotta:categorie_list')
    
    def get_context_data(self, **kwargs):
        context = super(CategorieViewUpdate, self).get_context_data(**kwargs)
        context["titolo"] = "Aggiorna Categorie"
        return context    
"""