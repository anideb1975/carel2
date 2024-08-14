from django.urls import path
from . import views

app_name='wizard'

urlpatterns = [
   path('wizard/',views.MarelliWizard.as_view(),name='wizard')
]

