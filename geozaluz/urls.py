from django.contrib import admin
from django.urls import path
from geology.views import horizons_list, density_list
from seismic_params.views import params_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', horizons_list, name='home'),
    path('horizons/', horizons_list, name='horizons'),
    path('params/', params_list, name='seismic_params_list'),
    path('density/', density_list, name='density_list'),
]
