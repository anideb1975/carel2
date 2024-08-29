from django.urls import path
from . import views

app_name='wizard'

urlpatterns = [
   path('wizard/',views.CarelWizard.as_view(),name='wizard'),
]

