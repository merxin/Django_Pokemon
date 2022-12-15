"""Pokemon URL Configuration

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
from django.urls import path, include,re_path
from pokedex.views import *
import re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', filter, name='filter'),
    path('category/<name>/', category, name='category'),
    path('pokemon/<name>/', pokemon, name='pokemon'),
    re_path(r'filter/', filter, name='filter'),
    re_path(r'comparison/', comparison, name='comparison'),
    ]
