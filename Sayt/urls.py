"""
URL configuration for Sayt project.

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


from .views import Home, Clock, PythonAnywhere, GitHub, WhiteNoise, AboutGadget


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('about-gadget/', AboutGadget.as_view(), name='about-gadget'),
    path('clock/', Clock.as_view(), name='clock'),
    path('pythonanywhere/', PythonAnywhere.as_view(), name='pythonanywhere'),
    path('github/', GitHub.as_view(), name='github'),
    path('whitenoise/', WhiteNoise.as_view(), name='whitenoise'),
]
