"""autos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from mainapp import views

#from pages import views as pages_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= "index"),
    path('inicio/', views.index, name= "inicio"),
    path('save-vehicle/', views.save_vehicle, name= "save"),
    path('create-vehicle/', views.create_vehicle, name= "create"),
    path('get-vehicle/', views.get_vehicles, name= "vehicles"),
    path('create-full-vehicle/', views.create_full_vehicle, name= "create_full"),
    path('habilitar/', views.habilitar, name= "habilitar"),


    path('disable/<int:id>', views.disable_vehicle, name= "disable"),
    path('enable-vehicle/<int:id>', views.enable_vehicle, name="enable"),
    path('edit-vehicle/<int:id>', views.update_vehicle, name= "edit"),
    path('filter-vehicle', views.filter, name= "filter"),
]
