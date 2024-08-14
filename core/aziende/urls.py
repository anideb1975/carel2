from django.urls import path
from . import views

app_name='aziende'

urlpatterns = [
    path('crea-aziende/', views.AziendeViewCreate.as_view(), name='stabilimenti_create'),
    path('lista-aziende/', views.AziendeViewList.as_view(), name='stabilimenti_list'),
    path('update-aziende/<int:pk>/', views.AziendeViewUpdate.as_view(), name='stabilimenti_update'),
    path('detail-aziende/<int:pk>/', views.AziendeViewDetail.as_view(), name='stabilimenti_detail'),
    path('delete-aziende/<int:pk>/', views.AziendeViewDelete.as_view(), name='stabilimenti_delete'),
]

urlpatterns += [
    path('crea-ute/', views.UteViewCreate.as_view(), name='ute_create'),
    path('lista-ute/', views.UteViewList.as_view(), name='ute_list'),
    path('update-ute/<int:pk>/', views.UteViewUpdate.as_view(), name='ute_update'),
    path('detail-ute/<int:pk>/', views.UteViewDetail.as_view(), name='ute_detail'),
    path('delete-ute/<int:pk>/', views.UteViewDelete.as_view(), name='ute_delete'),
]

urlpatterns += [
    path('crea-reparti/', views.RepartiViewCreate.as_view(), name='reparti_create'),
    path('lista-reparti/', views.RepartiViewList.as_view(), name='reparti_list'),
    path('update-reparti/<int:pk>/', views.RepartiViewUpdate.as_view(), name='reparti_update'),
    path('detail-reparti/<int:pk>/', views.RepartiViewDetail.as_view(), name='reparti_detail'),
    path('delete-reparti/<int:pk>/', views.RepartiViewDelete.as_view(), name='reparti_delete'),
]

