"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import (index,  monstrar_familiares, BuscarBebes, BuscarPadres, BuscarHijos, ActualizarBebe, ActualizarHijo, ActualizarPadre, AltaFamiliar, FamiliarDetalle, HijosDetalle, PadresDetalle, FamiliarList, HijosList, PadresList, FamiliarCrear, HijosCrear, PadresCrear, FamiliarBorrar, HijosBorrar, PadresBorrar, FamiliarActualizar, HijosActualizar, PadresActualizar)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('listas/', monstrar_familiares),
    path('bebe/buscar', BuscarBebes.as_view()),
    path('padre/buscar', BuscarPadres.as_view()),
    path('hijo/buscar', BuscarHijos.as_view()),
    path('bebes/actualizar/<int:pk>', ActualizarBebe.as_view()),
    path('hijos/actualizar/<int:pk>', ActualizarHijo.as_view()),
    path('padre/actualizar/<int:pk>', ActualizarPadre.as_view()),
    path('familiar/alta', AltaFamiliar.as_view()),
    path('panel-bebes/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path('panel-hijos/<int:pk>/detalle', HijosDetalle.as_view()),
    path('panel-padres/<int:pk>/detalle', PadresDetalle.as_view()),
    path('panel-bebes/', FamiliarList.as_view()),
    path('panel-hijos/', HijosList.as_view()),
    path('panel-padres/', PadresList.as_view()),
    path('panel-bebes/crear', FamiliarCrear.as_view()),
    path('panel-hijos/crear', HijosCrear.as_view()),
    path('panel-padres/crear', PadresCrear.as_view()),
    path('panel-bebes/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-hijos/<int:pk>/borrar', HijosBorrar.as_view()),
    path('panel-padres/<int:pk>/borrar', PadresBorrar.as_view()),
    path('panel-bebes/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('panel-hijos/<int:pk>/actualizar', HijosActualizar.as_view()),
    path('panel-Padres/<int:pk>/actualizar', PadresActualizar.as_view()),
]
