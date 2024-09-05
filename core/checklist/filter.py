from django_filters.filterset import FilterSet
from .models import CheckList, Controlli


class ChecklistFilter(FilterSet):
    class Meta:
        model = CheckList
        fields = ['turno', 'operatore']

class ControlliFilter(FilterSet):
    class Meta:
        model = Controlli
        fields = ['id_mezzo']        