from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def home(request):
    return redirect('inspecciones:dashboard')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('inspecciones/', include('inspecciones.urls')),
]