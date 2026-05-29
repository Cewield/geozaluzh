from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Сайт працює!</h1><p>Якщо ви це бачите, Django налаштовано правильно.</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
