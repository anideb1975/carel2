from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, 
                                  ListView, 
                                  DeleteView, 
                                  UpdateView, 
                                  DetailView,
                                  )

from django.contrib.auth.mixins import (LoginRequiredMixin, 
                                        UserPassesTestMixin,
)


from django.utils.translation import gettext_lazy as _
from django.views.generic.dates import (YearArchiveView,
                                        ArchiveIndexView,
                                        MonthArchiveView,
                                        WeekArchiveView,
                                        TodayArchiveView,
                                        )

from .forms import (CheckListForm, 
                    ControlliForm,
                    AnomalieControlliForm,
                    )

from .models import CheckList, Controlli

from view_breadcrumbs import (DetailBreadcrumbMixin, 
                              ListBreadcrumbMixin, 
                              DeleteBreadcrumbMixin, 
                              CreateBreadcrumbMixin,
                              UpdateBreadcrumbMixin,
                              BaseBreadcrumbMixin,
                            )
   
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
import datetime
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


### Crud Checklist ####

class ControlliInlineView(InlineFormSetFactory):
    model = Controlli
    form_class = ControlliForm
    #formset_class = BaseItemFormSet
    #initial = [{'name': 'example1'}, {'name', 'example2'}]
    #prefix = 'item-form'
    factory_kwargs = {'extra': 1, 'max_num': 1,
                      'can_order': False, 'can_delete': False}
    #formset_kwargs = {'auto_id': 'my_id_%s'}

class CheckListCrea(SuccessMessageMixin,LoginRequiredMixin,CreateBreadcrumbMixin,UserPassesTestMixin,CreateWithInlinesView):
    form_class = CheckListForm
    model = CheckList
    inlines = [ControlliInlineView]
    template_name = "checklist/create.html"
    #success_url = reverse_lazy('checklist:checklist_list')
    success_message = "Created successfully"

    def test_func(self):
        return self.request.user.role != "ASSISTENZA"

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('checklist:checklist_list')

    def get_success_url(self):
        return reverse_lazy('checklist:checklist_detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super(CheckListCrea, self).get_context_data(**kwargs)
        context["titolo"] = "Crea CheckList"
        return context
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.operatore = self.request.user
        self.object.save()
        return super().form_valid(form)
    
   
class CheckListLista(LoginRequiredMixin,ListBreadcrumbMixin,ListView):
    model = CheckList
    template_name = "checklist/list.html"
    context_object_name = 'checklists'
    
    def get_queryset(self):
        if (self.request.user.role == "ADMIN" or self.request.user.role == "RESPONSABILE"):
            qs = CheckList.objects.all()
        else:
            qs = CheckList.objects.filter(operatore=self.request.user)    
        return qs
     
    
    def get_context_data(self, **kwargs):
        context = super(CheckListLista, self).get_context_data(**kwargs)
        context["titolo"] = "Lista CheckLists"
        context['segment'] = "checklist_list"
        context['week'] = datetime.datetime.now()
        context['data_points'] =  [5, 4, 3, 7, 5, 10, 3]
        context['data_points2'] = [3, 2, 9, 5, 4, 6, 4]

        return context
    

class CheckListDettagli(LoginRequiredMixin,DetailBreadcrumbMixin,DetailView):
    model = CheckList
    template_name = "checklist/detail.html"
    context_object_name = 'checklist' 
    
    def get_context_data(self, **kwargs):
        context = super(CheckListDettagli, self).get_context_data(**kwargs)
        context["titolo"] = "Dettagli CheckList"
        #context["field"] = list(field.name.replace("_"," ") for field in self.object._meta.get_fields()if field.name not in ['id','operatore', 'turno', 'id_azienda', 'id_ute', 'id_reparto', 'id_categoria', 'id_mezzo', 'anomalie', 'creato', 'aggiornato', 'controlli_ptr'])
        return context


class CheckListModifica(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,UpdateBreadcrumbMixin,UpdateWithInlinesView):
    form_class = CheckListForm
    model = CheckList
    inlines = [ControlliInlineView]
    context_object_name = 'checklist'
    success_url = reverse_lazy('checklist:checklist_list')
    template_name = "checklist/update.html"
    success_message = "Update successfully"

    def test_func(self):
        return self.get_object().operatore == self.request.user or self.request.user.role == 'ADMIN' or  self.request.user.role != "ASSISTENZA"

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('checklist:checklist_list')
    
    
    def get_context_data(self, **kwargs):
        context = super(CheckListModifica, self).get_context_data(**kwargs)
        context["titolo"] = "Modifica Checklist"
        return context

    def form_valid(self, form):
        form.instance.operatore = self.request.user
        return super().form_valid(form)


class CheckListDelete(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,DeleteBreadcrumbMixin,DeleteView):
    model = CheckList
    template_name = "checklist/delete.html"
    context_object_name = 'checklist'
    success_message = 'Checklist cancellata'
    success_url = reverse_lazy('checklist:checklist_list')
    success_message = "Delete successfully"
    
    
    def test_func(self):
        return self.get_object().operatore == self.request.user or self.request.user.role == 'ADMIN'

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('checklist:checklist_list')  
    
    def get_context_data(self, **kwargs):
        context = super(CheckListDelete, self).get_context_data(**kwargs)
        context["titolo"] = "Cancella Cheklist"
        return context

### Fine crud checklist ###

###  Anomalie ###

class AnomalieListView(LoginRequiredMixin,ListBreadcrumbMixin,ListView):
    model = Controlli
    template_name = 'checklist/anomalie.html'
    context_object_name = 'anomalie'

    def get_queryset(self):
        return Controlli.objects.exclude(anomalie='').exclude(anomalie=None).all()
    
    def get_context_data(self, **kwargs):
        context = super(AnomalieListView, self).get_context_data(**kwargs)
        context["titolo"] = "Anomalie"
        context['segment'] = "assistenza"
        return context

class AnomalieDetailView(LoginRequiredMixin, DeleteBreadcrumbMixin, DeleteView):
    model = Controlli
    template_name = 'checklist/detail_anomalie.html'

    def get_context_data(self, **kwargs):
        context = super(AnomalieDetailView, self).get_context_data(**kwargs)
        context["titolo"] = "Dettagli Anomalie"
        return context

class AnomalieUpdateView(SuccessMessageMixin,LoginRequiredMixin, UserPassesTestMixin,UpdateBreadcrumbMixin, UpdateView):
    model = Controlli
    form_class = AnomalieControlliForm
    success_url = reverse_lazy('checklist:controlli_list')
    template_name = 'checklist/update_anomalie.html'
    success_message = "Update successfully"

    def test_func(self):
        return self.get_object().id_checklist.operatore== self.request.user or self.request.user.role == 'ADMIN'

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('checklist:controlli_list')

    def get_context_data(self, **kwargs):
        context = super(AnomalieUpdateView, self).get_context_data(**kwargs)
        context["titolo"] = "Dettagli Anomalie"
        return context    


### Fine  anomalie ###

# Vista Giornaliera

class CheckListTodayArchiveView(LoginRequiredMixin,BaseBreadcrumbMixin,TodayArchiveView):
    model = CheckList
    queryset = CheckList.objects.all()
    date_field = "creato"
    allow_future = True
    allow_empty = True
    template_name = 'checklist/giornaliero.html'
    context_object_name = 'checklists'
    crumbs = [("Giornaliero", reverse_lazy("checklist_giornaliero"))]
    
    def get_context_data(self, **kwargs):
        context = super(CheckListTodayArchiveView, self).get_context_data(**kwargs)
        context["titolo"] = "Giornaliero"
        context["segment"] = "checklist_list"
        return context


### Archivio ###

class CheckListArchivioView(LoginRequiredMixin,BaseBreadcrumbMixin,ArchiveIndexView):
    model = CheckList
    queryset = CheckList.objects.all()
    date_field = 'creato'
    allow_future = True
    allow_empty = True
    template_name = 'checklist/archivio.html'
    context_object_name = 'checklists'
    crumbs = [("Archivio", reverse_lazy("checklist_archivio"))]
    
    def get_context_data(self, **kwargs):
        context = super(CheckListArchivioView, self).get_context_data(**kwargs)
        context["titolo"] = "Archivio"
        context["segment"] = "checklist_list"
        return context

### VIsta Settimanale ###


class CheckListWeekArchiveView(WeekArchiveView):
    queryset = CheckList.objects.all()
    date_field = "creato"
    week_format = "%W"
    allow_future = True
    allow_empty  = True
    context_object_name = 'checklists'
    template_name = 'lcs/list.html'
    crumbs = [("checklist settimana", reverse_lazy("checklist_settimana"))]
    context_object_name = 'checklists'
    
    def get_context_data(self, **kwargs):
        context = super(CheckListYearArchiveView, self).get_context_data(**kwargs)
        context["titolo"] = "Vista Settimana"
        context["segment"] = "checklist_list"
        return context



## Vista Annuale ###


class CheckListYearArchiveView(LoginRequiredMixin,YearArchiveView):
    model = CheckList
    queryset = CheckList.objects.all()
    date_field = "creato"
    make_object_list = True
    allow_future = True
    allow_empty  = True
    template_name = 'lcs/list.html'
    crumbs = [("checklist anno", reverse_lazy("checklist_anno"))]
    context_object_name = 'checklists'
    
    def get_context_data(self, **kwargs):
        context = super(CheckListYearArchiveView, self).get_context_data(**kwargs)
        context["titolo"] = "Vista Annuale"
        context["segment"] = "checklist_list"
        return context

### Vista Mensile ###

class CheckListMonthsArchiveView(LoginRequiredMixin,MonthArchiveView):
    model = CheckList
    queryset = CheckList.objects.all()
    date_field = "creato"
    make_object_list = True
    allow_future = True
    allow_empty  = True
    template_name = 'lcs/list_mese.html'
    crumbs = [("checklist mese", reverse_lazy("checklist_mese"))]
    context_object_name = 'checklists'
    
    def get_context_data(self, **kwargs):
        context = super(CheckListMonthsArchiveView, self).get_context_data(**kwargs)
        context["titolo"] = "Vista Mensile"
        context["segment"] = "checklist_list"
        return context    
    


""" class CheckListModifica(SweetifySuccessMixin,LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = CheckList
    form_class = CheckListForm
    success_message = 'Checklist modificata con successo!'
    template_name = "checklist/update.html"
    context_object_name = 'checklist'
    success_url = reverse_lazy('checklist:checklist_list')
    
    def test_func(self):
        return self.get_object().operatore == self.request.user or self.request.user.role == 'ADMIN'

    def handle_no_permission(self):
        sweetify.warning(self.request, 'Utente non autorizzato')
        return redirect('checklist:checklist_list')
    
    
    def get_context_data(self, **kwargs):
        context = super(CheckListModifica, self).get_context_data(**kwargs)
        context["titolo"] = "Modifica Checklist"
        return context

    def form_valid(self, form):
        form.instance.operatore = self.request.user
        return super().form_valid(form)     """

