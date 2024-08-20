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
     path("controlli-list/",views.ControlliListView.as_view(),name="controlli_list"),
     path("controlli-detail/<int:pk>/",views.ControlliDetailView.as_view(),name="controlli_detail"),
     path("controlli-update/<int:pk>/",views.ControlliUpdateView.as_view(),name="controlli_update"),
     path("controlli-delete/<int:pk>/",views.ControlliDeleteView.as_view(),name="controlli_delete"),
]

urlpatterns += [
     path("anomalie-list/",views.AnomalieListView.as_view(),name="controlli_anomalie"),
     path("anomalie-detail/<int:pk>/",views.AnomalieDetailView.as_view(),name="controlli_anomalie_detail"),
     path("anomalie-update/<int:pk>/",views.AnomalieUpdateView.as_view(),name="controlli_anomalie_update"),
     path("anomalie-delete/<int:pk>/",views.AnomalieDeleteView.as_view(),name="controlli_anomalie_delete"),
]

urlpatterns += [
    path("checklist-archivio/",views.CheckListArchivioView.as_view(),name="checklist_archivio"),
    path("checklist-giornaliero/",views.CheckListTodayArchiveView.as_view(),name="checklist_giornaliero"),
    path("checklist-anno/<int:year>/", views.CheckListYearArchiveView.as_view(), name='checklist_anno'),
    # Example: /2012/08/
    path("checklist-mese/<int:year>/<int:month>/",views.CheckListMonthsArchiveView.as_view(month_format="%m"),name='checklist_mese'),# Example: /2012/week/23/
    path("checklist-settimana/<int:year>/week/<int:week>/",views.CheckListWeekArchiveView.as_view(week_format = "%W"),name="checklist_settimana"),
]