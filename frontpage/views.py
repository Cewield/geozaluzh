from django.shortcuts import render
from django.db.models import Min, Max
from geology.models import GeologicalHorizon, DensityVelocity
from seismic_params.models import Seismic3DParams

def home(request):
    horizons_count = GeologicalHorizon.objects.count()
    min_depth_obj = GeologicalHorizon.objects.aggregate(Min('depth_min'))
    max_depth_obj = GeologicalHorizon.objects.aggregate(Max('depth_max'))
    min_depth = min_depth_obj['depth_min__min'] if min_depth_obj['depth_min__min'] else '—'
    max_depth = max_depth_obj['depth_max__max'] if max_depth_obj['depth_max__max'] else '—'
    params_count = Seismic3DParams.objects.count()
    
    context = {
        'horizons_count': horizons_count,
        'min_depth': min_depth,
        'max_depth': max_depth,
        'params_count': params_count,
    }
    return render(request, 'frontpage/home.html', context)