"""
URL configuration for tanfelo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app_tanfelo.views import tantargyak_feltoltese_view, tantargyak_feltoltese_kuld_view, tanarok_feltoltese_view, tanarok_feltoltese_kuld_view, kapcsolat_feltoltese_view, kapcsolat_feltoltese_kuld_view

urlpatterns = [
    path('admin/', admin.site.urls),

    #Tantárgyak
    path('tanfelo/feltoltes/tantargyak/', tantargyak_feltoltese_view),
    path('tanfelo/feltoltes/tantargyak/kuld/', tantargyak_feltoltese_kuld_view),

    #Tanárok
    path('tanfelo/feltoltes/tanarok/', tanarok_feltoltese_view),
    path('tanfelo/feltoltes/tanarok/kuld/', tanarok_feltoltese_kuld_view),

    #Kapcsolatok(tantargy-tanar)
    path('tanfelo/feltoltes/kapcsolat/', kapcsolat_feltoltese_view),
    path('tanfelo/feltoltes/kapcsolat/kuld/', kapcsolat_feltoltese_kuld_view),
]
