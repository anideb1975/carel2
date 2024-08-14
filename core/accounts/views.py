from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,DetailView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView


from django.contrib.auth import get_user_model
User = get_user_model()

from .forms import (CustomUserCreationForm,
                    CustomUserChangeForm,
                    AssistenzaCreationForm,
                    AssistenzaChangeForm,
                    OperatoreCreationForm,
                    OperatoreChangeForm,
                    ResponsabileCreationForm,
                    ResponsabileChangeForm,
                    AssistenzaCreationForm,
                    AssistenzaChangeForm,
                    CustomAdminCreationForm,
                    CustomAdminChangeForm,
                    ChangePasswordForm,
                    )

from view_breadcrumbs import (DetailBreadcrumbMixin, 
                              ListBreadcrumbMixin, 
                              DeleteBreadcrumbMixin, 
                              CreateBreadcrumbMixin,
                              UpdateBreadcrumbMixin,
)
   
from .models import (Admin, Operatore, Responsabile, Assistenza)   

### Cambia Password ##

class ChangePasswordView(LoginRequiredMixin,PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/password-change.html'

     
    def get_context_data(self, **kwargs):
        context = super(ChangePasswordView, self).get_context_data(**kwargs)
        context["titolo"] = "Cambia password"
        return context    

### Fine ###à



### Signup ####

class SignUpUser(SuccessMessageMixin,CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/create.html'
    success_message = "Created successfully"
    
    def get_context_data(self, **kwargs):
        context = super(SignUpUser, self).get_context_data(**kwargs)
        context["titolo"] = "Crea Utente"
        return context

class SignUpAdmin(SuccessMessageMixin,CreateView):
    form_class = CustomAdminCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/create.html'
    success_message = "Created successfully"
    
    def get_context_data(self, **kwargs):
        context = super(SignUpAdmin, self).get_context_data(**kwargs)
        context["titolo"] = "Crea Admin"
        return context


class SignUpOperatore(SuccessMessageMixin,CreateView):
    form_class  = OperatoreCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/create.html'
    success_message = "Created successfully"

    
    def get_context_data(self, **kwargs):
        context = super(SignUpOperatore, self).get_context_data(**kwargs)
        context["titolo"] = "Crea Operatore"
        return context
    

class SignUpResponsabile(SuccessMessageMixin,CreateView):
    form_class = ResponsabileCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/create.html'
    success_message = "Created successfully"
    
    def get_context_data(self, **kwargs):
        context = super(SignUpResponsabile, self).get_context_data(**kwargs)
        context["titolo"] = "Crea Responsabile"
        return context
    
class SignUpAssistenza(SuccessMessageMixin,CreateView):
    form_class = AssistenzaCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/create.html'
    success_message = "Created successfully"

    
    def get_context_data(self, **kwargs):
        context = super(SignUpAssistenza, self).get_context_data(**kwargs)
        context["titolo"] = "Crea Assistenza"
        return context
        
#### Lista ####

class ListaUserView(LoginRequiredMixin,ListBreadcrumbMixin, ListView):
    model = User
    template_name = 'accounts/list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ListaUserView, self).get_context_data(**kwargs)
        context["titolo"] = "Utenti"
        context["segment"] = "user"
        return context

class ListaAdminView(LoginRequiredMixin,ListBreadcrumbMixin, ListView):
    model = Admin
    template_name = 'accounts/list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ListaAdminView, self).get_context_data(**kwargs)
        context["titolo"] = "Admin"
        context["segment"] = "user"
        return context

class ListaOperatoreView(LoginRequiredMixin,ListBreadcrumbMixin, ListView):
    model = Operatore
    template_name = 'accounts/list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ListaOperatoreView, self).get_context_data(**kwargs)
        context["titolo"] = "Operatori"
        context["segment"] = "user"
        return context

class ListaResponsabiliView(LoginRequiredMixin,ListBreadcrumbMixin, ListView):
    model = Responsabile
    template_name = 'accounts/list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ListaResponsabiliView, self).get_context_data(**kwargs)
        context["titolo"] = "Responsabili"
        context["segment"] = "user"
        return context

class ListaAssistenzaView(LoginRequiredMixin,ListBreadcrumbMixin, ListView):
    model = Assistenza
    template_name = 'accounts/list.html'

    
    def get_context_data(self, **kwargs):
        context = super(ListaAssistenzaView, self).get_context_data(**kwargs)
        context["titolo"] = "Assistenza"
        context["segment"] = "user"
        return context

### Fine Lista ###

### Detail ####

class UserDetailView(LoginRequiredMixin,DetailBreadcrumbMixin, UpdateView):
    model = User
    fields = "__all__"
    template_name = 'accounts/profile.html'
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context["titolo"] = "Utenti"
        return context

class AdminDetailView(LoginRequiredMixin,DetailBreadcrumbMixin, DetailView):
    model = Admin
    fields = "__all__"
    template_name = 'accounts/profile.html'
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super(AdminDetailView, self).get_context_data(**kwargs)
        context["titolo"] ="Admin"
        return context 

class OperatoreDetailView(LoginRequiredMixin,DetailBreadcrumbMixin, DetailView):
    model = Operatore
    fields = "__all__"
    template_name = 'accounts/profile.html'
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super(OperatoreDetailView, self).get_context_data(**kwargs)
        context["titolo"] = "Operatori"
        return context 


class ResponsabileDetailView(LoginRequiredMixin,DetailBreadcrumbMixin, DetailView):
    model = Responsabile
    fields = "__all__"
    template_name = 'accounts/profile.html'
    context_object_name = "profile"


    def get_context_data(self, **kwargs):
        context = super(ResponsabileDetailView, self).get_context_data(**kwargs)
        context["titolo"] = "Responsabili"
        return context 

class AssistenzaDetailView(LoginRequiredMixin,DetailBreadcrumbMixin, DetailView):
    model = Assistenza
    fields = "__all__"
    context_object_name = "profile"
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super(AssistenzaDetailView, self).get_context_data(**kwargs)
        context["titolo"] = "Assistenza"
        return context 
    
## Fine detail ###

### Update ###


class UserUpdateView(SuccessMessageMixin,LoginRequiredMixin,UpdateBreadcrumbMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'accounts/update.html'
    success_url = reverse_lazy('accounts:user_list')
    context_object_name = "profile"
    success_message = "Update successfully"


    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context["titolo"] = "User"
        return context 

class AdminUpdateView(SuccessMessageMixin,LoginRequiredMixin,UpdateBreadcrumbMixin, UpdateView):
    model = Admin
    form_class = CustomAdminChangeForm
    template_name = 'accounts/update.html'
    success_url = reverse_lazy('accounts:user_list')
    context_object_name = "profile"
    success_message = "Update successfully"


    def get_context_data(self, **kwargs):
        context = super(AdminUpdateView, self).get_context_data(**kwargs)
        context["titolo"] = "Admin"
        return context 

class OperatoreUpdateView(SuccessMessageMixin,LoginRequiredMixin,UpdateBreadcrumbMixin, UpdateView):
    model = Operatore
    form_class = OperatoreChangeForm
    template_name = 'accounts/update.html'
    success_url = reverse_lazy('accounts:user_list')
    context_object_name = "profile"
    success_message ="Update successfully"

    def get_context_data(self, **kwargs):
        context = super(OperatoreUpdateView, self).get_context_data(**kwargs)
        context["titolo"] = "Operatore"
        return context 

class ResponsabileUpdateView(SuccessMessageMixin,LoginRequiredMixin,UpdateBreadcrumbMixin, UpdateView):
    model = Responsabile
    form_class = ResponsabileChangeForm
    template_name = 'accounts/update.html'
    success_url = reverse_lazy('accounts:user_list')
    context_object_name = "profile"
    success_message = "Update successfully"

    def get_context_data(self, **kwargs):
        context = super(ResponsabileUpdateView, self).get_context_data(**kwargs)
        context["titolo"] = "Responsabile"
        return context 

class AssistenzaUpdateView(SuccessMessageMixin,LoginRequiredMixin,UpdateBreadcrumbMixin, UpdateView):
    model = Assistenza
    form_class = AssistenzaChangeForm
    template_name = 'accounts/update.html'
    success_url = reverse_lazy('accounts:user_list')
    context_object_name = "profile"
    success_message = "Update successfully"

    def get_context_data(self, **kwargs):
        context = super(AssistenzaUpdateView, self).get_context_data(**kwargs)
        context["titolo"] ="Assistenza"
        return context 

### fine Update ####

""" class UpdateUtentiView(LoginRequiredMixin,UserPassesTestMixin,UpdateBreadcrumbMixin, UpdateView):
    model = User
    fields = ['username','first_name','last_name','badge','avatar']
    template_name = 'accounts/update.html'
    success_url = reverse_lazy('accounts:user_list')
    context_object_name = 'utenti'
    
    def test_func(self):
        return self.get_object().id == self.request.user.id or self.request.user.role == 'ADMIN'

    def handle_no_permission(self):
        return redirect('accounts:user_list')  
    
    def get_context_data(self, **kwargs):
        context = super(UpdateUtentiView, self).get_context_data(**kwargs)
        context["titolo"] = "Modifica Utenti"
        return context
 """

""" class DeleteUtentiView(LoginRequiredMixin,UserPassesTestMixin,DeleteBreadcrumbMixin,DeleteView):
    model = User
    template_name = 'accounts/delete.html'
    success_url = reverse_lazy('accounts:user_list')
    context_object_name = 'utente'
    
    def test_func(self):
        return self.request.user.role == 'ADMIN'

    
    def handle_no_permission(self):
        return redirect('accounts:user_list')
    
    
    def get_context_data(self, **kwargs):
        context = super(DeleteUtentiView, self).get_context_data(**kwargs)
        context["titolo"] = "Cancella Aziende"
        return context 
 """


# Da Implementare
    
""" def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)    
     """