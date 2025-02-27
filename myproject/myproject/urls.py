"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('tablesdata/', views.tablesdata, name='tablesdata'),
    path('tablesgeneral/', views.tablesgeneral, name='tablesgeneral'),
    
    path('chartschartjs/', views.chartschartjs, name='chartschartjs'),
    path('chartsapexcharts/', views.chartsapexcharts, name='chartsapexcharts'),
    path('chartsecharts/', views.chartsecharts, name='chartsecharts'),
     
    path('usersprofile/', views.usersprofile, name='usersprofile'),
    path('pagescontact/', views.pagescontact, name='pagescontact'),
    path('pagesregister/', views.pagesregister, name='pagesregister'),
    path('pageslogin/', views.pageslogin, name='pageslogin'),
     
    path('countries/', views.countries, name='countries'),
    path('unitedstates/', views.countries, name='unitedstates'),
    
    path('home/', views.home, name='home'),
    path('newsheadlines/', views.index, name='index'),
    
    path('upload_csv/', views.upload_csv, name='upload_csv'),
    path('fetch_data/', views.fetch_data, name='fetch_data'),
    path('data_list/', views.data_list, name='data_list'),
]

