from django.shortcuts import render
from .models import GeologicalHorizon

def horizons_list(request):
    horizons = GeologicalHorizon.objects.all().order_by('depth_min')
    return render(request, 'geology/horizons.html', {'horizons': horizons})
from .models import DensityVelocity

def density_list(request):
    densities = DensityVelocity.objects.all()
    return render(request, 'geology/density_list.html', {'densities': densities})
