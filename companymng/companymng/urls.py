"""
URL configuration for companymng project.

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
from account.views import hello,luminar,land,logi,regis,sample,employee,home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home"),
    path('sample',hello),
    path('Luminar', luminar),
    path('htmlresponse',land),
    path('login',logi,name="login"),
    path('register',regis,name="regisurl"),
    path('Python',sample,name="sample"),
    path('employee',employee,name="empurl")
    
]
