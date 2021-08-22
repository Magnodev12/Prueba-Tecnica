"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from personas import views as vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , vista.inicio , name = 'inicio') ,
    path('crear_persona' , vista.crear_persona) ,
    path('actualizar_persona_<int:id>' , vista.actualizar_persona) ,
    path('detail_persona_<int:id>' , vista.detail) ,
    path('borrar_persona_<int:id>' , vista.borrar_persona) ,

]
