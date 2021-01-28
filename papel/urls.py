"""papel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from inventario import views as views_inven
from ventas import views as views_ven

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', views_inven.inven, name = 'bodega'),
    path('ventas/', views_ven.sales, name = 'sale'),
    path('listarv/', views_ven.ventasList, name = 'listav'),
    path('listarin/', views_inven.invenList, name = 'listain'),
    path('dia/',views_ven.gananciaDiaria, name = 'gdiaria'),
    path('editarv/<int:id_venta>/',views_ven.ventaEdit,name = 'editv'),
    path('borrarv/<int:id_venta>/',views_ven.ventaBorr,name = 'delv'),
]
