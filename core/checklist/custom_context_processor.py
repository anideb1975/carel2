from .models import Controlli, CheckList

def fanomalie(request):
    anomalie = Controlli.objects.exclude(anomalie='').exclude(anomalie=None).order_by('-creato')[:4]
    context = {'anomalie':anomalie}
    return(context)

def anni(request):
    anni = CheckList.objects.all().dates('creato', 'year')
    anno = [y.year for y in anni]
    context = {'anni': anno}
    return(context)

def mesi(request):
    mesi = CheckList.objects.all().dates('creato', 'month')
    years = CheckList.objects.all().dates('creato', 'year')
    mese= [m.month for m in mesi]
    context = {'mesi': mese, 'years':years}
    return(context)

def settimane(request):
    settimane = CheckList.objects.all().dates('creato', 'week')
    years = CheckList.objects.all().dates('creato', 'year')
    context = {'settimane':settimane, 'years':years}
    return(context)