from django.urls import path
from . import views


app_name='checklist'

urlpatterns = [
    path("lista-checklist/", views.CheckListLista.as_view(), name="checklist_list"),
    path("crea-checklist/", views.CheckListCrea.as_view(), name="checklist_create"),
    path("detail-checklist/<int:pk>/", views.CheckListDettagli.as_view(), name="checklist_detail"),
    path("update-checklist/<int:pk>/", views.CheckListModifica.as_view(), name="checklist_update"),
    path("delete-checklist/<int:pk>/", views.CheckListDelete.as_view(), name="checklist_delete"),
]

urlpatterns += [
    path("checklist-archivio/",views.CheckListArchivioView.as_view(),name="checklist_archivio"),
    path("checklist-giornaliero/",views.CheckListTodayArchiveView.as_view(),name="checklist_giornaliero"),
]

urlpatterns += [
     path("controlli-list/",views.AnomalieListView.as_view(),name="controlli_list"),
     path("controlli-detail/<int:pk>/",views.AnomalieDetailView.as_view(),name="controlli_detail"),
     path("controlli-update/<int:pk>/",views.AnomalieUpdateView.as_view(),name="controlli_update"),
]
