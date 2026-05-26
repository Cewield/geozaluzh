from django.shortcuts import render
from .models import Seismic3DParams

def params_list(request):
    params = Seismic3DParams.objects.all()
    return render(request, 'seismic_params/params_list.html', {'params': params})
