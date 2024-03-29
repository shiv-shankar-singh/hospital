"""hospital URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.site.site_header='CardioCare Heart Hospital Admin'
admin.site.site_title= 'CardioCare Heart Hospital Admin Portal'
admin.site.index_title = 'WELCOME TO CARDIOCARE HEART HOSPITAL ADMIN PORTAL'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('appoint', views.appoint, name="appoint"),
    path('contactus', views.contactus, name="contactus"),
    path('read', views.read, name='read'),
    path('contact', views.contacts, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()