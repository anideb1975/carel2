from django.urls import path
from . import views

app_name='accounts'


## SignUP ###
urlpatterns = [
    path('user-create/', views.SignUpUser.as_view(), name='user_create'),
    path('admin-create/', views.SignUpAdmin.as_view(), name='admin_create'),
    path('operatore-create/', views.SignUpOperatore.as_view(), name='operatore_create'),
    path('responsabile-create/', views.SignUpResponsabile.as_view(), name='responsabile_create'),
    path('assistenza-create/', views.SignUpAssistenza.as_view(), name='assistenza_create'),
]


### Update ####
urlpatterns += [
    path('user-update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('admin-update/<int:pk>/', views.AdminUpdateView.as_view(), name='admin_update'),
    path('operatore-update/<int:pk>/', views.OperatoreUpdateView.as_view(), name='operatore_update'),
    path('responsabile-update/<int:pk>/', views.ResponsabileUpdateView.as_view(), name='responsabile_update'),
    path('assistenza-update/<int:pk>/', views.AssistenzaUpdateView.as_view(), name='assistenza_update'),
]

### Detail ###
urlpatterns += [
    path('user-detail/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('admin-detail/<int:pk>/', views.AdminDetailView.as_view(), name='admin_detail'),
    path('operatore-detail/<int:pk>/', views.OperatoreDetailView.as_view(), name='operatore_detail'),
    path('responsabile-detail/<int:pk>/', views.ResponsabileDetailView.as_view(), name='responsabile_detail'),
    path('assistenza-detail/<int:pk>/', views.AssistenzaDetailView.as_view(), name='assistenza_detail'),
]

### List ###
urlpatterns += [
    path('user-list/', views.ListaUserView.as_view(), name='user_list'),
    path('admin-list/', views.ListaAdminView.as_view(), name='admin_list'),
    path('operatori-list/', views.ListaOperatoreView.as_view(), name='operatore_list'),
    path('responsabili-list/', views.ListaResponsabiliView.as_view(), name='responsabile_list'),
    path('manutenzione-list/', views.ListaAssistenzaView.as_view(), name='assistenza_list'),
]

urlpatterns += [
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
]