"""
URL configuration for Gym project.

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
from main_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('blog/', blog),
    path('home/', home),
    path('about/', about),
    path('bmi-calculator/', bmi),
    path('contact/', contact),
    path('success/', success),
    path('test/', test),
    path('Khabar1/', khabar1),
    path('Khabar2/', khabar2),
    path('Khabar3/', khabar3),
    path('Khabar4/', khabar4),
    path('Khabar5/', khabar5),
    path('Khabar6/', khabar6),
    path('Khabar7/', khabar7),
    path('shahrie', Shahrie),
    path('layout', layout),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

