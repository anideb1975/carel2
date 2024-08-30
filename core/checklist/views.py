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
from .models import Controlli as Anomalie

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
from django.db.models.functions import ExtractYear,ExtractMonth, ExtractDay, ExtractWeek, ExtractIsoYear


### Crud Checklist ####

class ControlliInlineView(InlineFormSetFactory):
    model = Controlli
    form_class = ControlliForm
    #formset_class = InlineFormSet
    #initial = [{'name': 'example1'}, {'name', 'example2'}]
    prefix = 'form'
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
        context["titolo"] = "CheckLists"
        context['segment'] = "checklist_list"
        context['anni'] = CheckList.objects.annotate(year=ExtractYear('creato')).values('year').order_by('-year').distinct()
        context['mesi'] = CheckList.objects.annotate(month=ExtractMonth('creato')).values('month').order_by('-month').distinct()
        context['settimane'] = CheckList.objects.annotate(week=ExtractWeek('creato')).values('week').order_by('-week').distinct()
        context['anni_mesi'] = zip(context['anni'],context['mesi'])
        context['anni_settimane'] = zip(context['anni'],context['settimane'])
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
    #success_url = reverse_lazy('checklist:checklist_list')
    template_name = "checklist/update.html"
    success_message = "Update successfully"
   
    def get_success_url(self):
        return reverse_lazy('checklist:checklist_list')

    def test_func(self):
        return self.get_object().operatore == self.request.user or self.request.user.role == 'ADMIN' or  self.request.user.role != "ASSISTENZA"

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('checklist:checklist_list')
    
    
    def get_context_data(self, **kwargs):
        context = super(CheckListModifica, self).get_context_data(**kwargs)
        context["titolo"] = "Modifica Checklist"
        return context

  


class CheckListDelete(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,DeleteBreadcrumbMixin,DeleteView):
    model = CheckList
    template_name = "checklist/delete.html"
    context_object_name = 'checklist'
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
    model = Anomalie
    template_name = 'checklist/anomalie.html'
    context_object_name = 'anomalie'

    def get_queryset(self):
        return Anomalie.objects.exclude(anomalie='').exclude(anomalie=None).all().order_by('-creato')
    
    def get_context_data(self, **kwargs):
        context = super(AnomalieListView, self).get_context_data(**kwargs)
        context["titolo"] = "Controlli Anomalie"
        context['segment'] = "assistenza"
        return context

class AnomalieDetailView(LoginRequiredMixin, DetailBreadcrumbMixin, DeleteView):
    model = Anomalie
    template_name = 'checklist/detail_anomalie.html'
    #crumbs = [("checklist settimana", reverse_lazy("checklist:checklist:checklist_settimana"))]


    def get_context_data(self, **kwargs):
        context = super(AnomalieDetailView, self).get_context_data(**kwargs)
        context["titolo"] = "Dettagli Anomalie"
        return context

class AnomalieUpdateView(SuccessMessageMixin,LoginRequiredMixin, UserPassesTestMixin,UpdateBreadcrumbMixin, UpdateView):
    model = Anomalie
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

    def form_valid(self, form):
        form.instance.operatore = self.request.user
        return super().form_valid(form)    

class AnomalieDeleteView(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,DeleteBreadcrumbMixin,DeleteView):
    model = Anomalie
    form_class = AnomalieControlliForm
    template_name = "checklist/delete_anomalia.html"
    context_object_name = 'checklist'
    success_url = reverse_lazy('checklist:controlli_anomalie')
    success_message = "Delete successfully"
    
    
    def test_func(self):
        return self.get_object().operatore == self.request.user or self.request.user.role == 'ADMIN'

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('checklist:controlli_anomalia')  
    
    def get_context_data(self, **kwargs):
        context = super(AnomalieDeleteView, self).get_context_data(**kwargs)
        context["titolo"] = "Cancella Anomalia"
        return context

### Fine  anomalie ###


###  Controlli ###

class ControlliListView(LoginRequiredMixin,ListBreadcrumbMixin,ListView):
    model = Controlli
    template_name = 'checklist/controlli/list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ControlliListView, self).get_context_data(**kwargs)
        context["titolo"] = "Controlli"
        context['segment'] = "checklist_list"
        return context

class ControlliDetailView(LoginRequiredMixin, DetailBreadcrumbMixin, DeleteView):
    model = Controlli
    template_name = 'checklist/controlli/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ControlliDetailView, self).get_context_data(**kwargs)
        context["titolo"] = "Dettagli Controlli"
        return context

class ControlliUpdateView(SuccessMessageMixin,LoginRequiredMixin, UserPassesTestMixin,UpdateBreadcrumbMixin, UpdateView):
    model = Controlli
    form_class = ControlliForm
    success_url = reverse_lazy('checklist:controlli_list')
    template_name = 'checklist/controlli/update.html'
    success_message = "Update successfully"

    def test_func(self):
        return self.get_object().id_checklist.operatore== self.request.user or self.request.user.role == 'ADMIN'

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('checklist:controlli_list')

    def get_context_data(self, **kwargs):
        context = super(ControlliUpdateView, self).get_context_data(**kwargs)
        context["titolo"] = "Dettagli Controllo"
        return context
    def form_valid(self, form):
        form.instance.id_checklist.operatore = self.request.user
        return super().form_valid(form)        

class ControlliDeleteView(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,DeleteBreadcrumbMixin,DeleteView):
    model = Controlli
    template_name = "checklist/controlli/delete.html"
    success_url = reverse_lazy('checklist:controlli_list')
    success_message = "Delete successfully"
    
    
    def test_func(self):
        return self.get_object().id_checklist.operatore == self.request.user or self.request.user.role == 'ADMIN'

    def handle_no_permission(self):
        messages.warning(self.request, "Not Authorized")
        return redirect('checklist:controlli_list')  
    
    def get_context_data(self, **kwargs):
        context = super(ControlliDeleteView, self).get_context_data(**kwargs)
        context["titolo"] = "Cancella Controllo"
        return context

    def form_valid(self, form):
        object = self.object.id_checklist.id
        chk = CheckList.objects.get(id=object)
        chk.delete()
        return super().form_valid(form)

### Fine  controlli ###

# Vista Giornaliera

class CheckListTodayArchiveView(LoginRequiredMixin,ListBreadcrumbMixin,TodayArchiveView):
    model = CheckList
    queryset = CheckList.objects.all()
    date_field = "creato"
    allow_future = True
    allow_empty = True
    template_name = 'checklist/giornaliero.html'
    context_object_name = 'checklists'
    
    def get_context_data(self, **kwargs):
        context = super(CheckListTodayArchiveView, self).get_context_data(**kwargs)
        context["titolo"] = "Giornaliero"
        context["segment"] = "checklist_list"
        return context


### Archivio ###

class CheckListArchivioView(LoginRequiredMixin,ListBreadcrumbMixin,ArchiveIndexView):
    model = CheckList
    queryset = CheckList.objects.all()
    date_field = 'creato'
    allow_future = True
    allow_empty = True
    template_name = 'checklist/archivio.html'
    context_object_name = 'checklists'
    
    def get_context_data(self, **kwargs):
        context = super(CheckListArchivioView, self).get_context_data(**kwargs)
        context["titolo"] = "Archivio"
        context["segment"] = "checklist_list"
        return context

### VIsta Settimanale ###


class CheckListWeekArchiveView(LoginRequiredMixin,ListBreadcrumbMixin,WeekArchiveView):
    model = CheckList
    queryset = CheckList.objects.all()
    date_field = "creato"
    week_format = "%W"
    allow_future = True
    allow_empty  = True
    template_name = 'checklist/lista_settimana.html'
    #crumbs = [("checklist settimana", reverse_lazy("checklist:checklist:checklist_settimana"))]
    context_object_name = 'checklists'
    
    def get_context_data(self, **kwargs):
        context = super(CheckListWeekArchiveView, self).get_context_data(**kwargs)
        context["titolo"] = "Vista Settimana"
        context["segment"] = "checklist_list"
        context['anni'] = CheckList.objects.dates('creato', 'year').annotate()
        context['mesi'] = CheckList.objects.dates('creato', 'month').annotate()
        context['settimane'] = CheckList.objects.dates('creato', 'week').annotate()
        context['anni_mesi'] = zip(context['anni'],context['mesi'])
        context['anni_settimane'] = zip(context['anni'],context['settimane'])
        return context



## Vista Annuale ###


class CheckListYearArchiveView(LoginRequiredMixin,ListBreadcrumbMixin,YearArchiveView):
    model = CheckList
    queryset = CheckList.objects.all()
    date_field = "creato"
    make_object_list = True
    allow_future = True
    allow_empty  = True
    template_name = 'checklist/lista_anno.html'
    context_object_name = 'checklists'
    
    def get_context_data(self, **kwargs):
        context = super(CheckListYearArchiveView, self).get_context_data(**kwargs)
        context["titolo"] = "Vista Anno"
        context["segment"] = "checklist_list"
        context['week'] = datetime.datetime.now()
        context['anni'] = CheckList.objects.dates('creato', 'year').annotate()
        context['mesi'] = CheckList.objects.dates('creato', 'month').annotate()
        context['settimane'] = CheckList.objects.dates('creato', 'week').annotate()
        context['anni_mesi'] = zip(context['anni'],context['mesi'])
        context['anni_settimane'] = zip(context['anni'],context['settimane'])
        return context

### Vista Mensile ###

class CheckListMonthsArchiveView(LoginRequiredMixin,ListBreadcrumbMixin,MonthArchiveView):
    model = CheckList
    queryset = CheckList.objects.all()
    date_field = "creato"
    make_object_list = True
    allow_future = True
    allow_empty  = True
    template_name = 'checklist/lista_mese.html'
    context_object_name = 'checklists'
    
    def get_context_data(self, **kwargs):
        context = super(CheckListMonthsArchiveView, self).get_context_data(**kwargs)
        context["titolo"] = "Vista Mensile"
        context["segment"] = "checklist_list"
        context['anni'] = CheckList.objects.dates('creato', 'year').annotate()
        context['mesi'] = CheckList.objects.dates('creato', 'month').annotate()
        context['settimane'] = CheckList.objects.dates('creato', 'week').annotate()
        context['anni_mesi'] = zip(context['anni'],context['mesi'])
        context['anni_settimane'] = zip(context['anni'],context['settimane'])
        return context    
