from dal import autocomplete

from flotta.models import Mezzi


class MezzoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Mezzi.objects.none()

        qs = Mezzi.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs