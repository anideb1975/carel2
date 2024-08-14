from django.urls import path
from . import views

app_name='assistenza'


### Aziende ###

urlpatterns = [
    path('crea-aziende/', views.AziendeViewCreate.as_view(), name='aziende_create'),
    path('lista-aziende/', views.AziendeViewList.as_view(), name='aziende_list'),
    path('update-aziende/<int:pk>/', views.AziendeViewUpdate.as_view(), name='aziende_update'),
    path('detail-aziende/<int:pk>/', views.AziendeViewDetail.as_view(), name='aziende_detail'),
    path('delete-aziende/<int:pk>/', views.AziendeViewDelete.as_view(), name='aziende_delete'),
]

### Interventi ###

urlpatterns += [
    path('crea-interventi/<int:pk>/', views.InterventiCreateView.as_view(), name='interventi_create'),
    path('lista-interventi/', views.InterventiViewList.as_view(), name='interventi_list'),
    path('update-interventi/<int:pk>/', views.InterventiUpdateView.as_view(), name='interventi_update'),
    path('detail-interventia/<int:pk>/', views.InterventiViewDetail.as_view(), name='interventi_detail'),
    path('delete-interventi/<int:pk>/', views.InterventiViewDelete.as_view(), name='interventi_delete'),
]