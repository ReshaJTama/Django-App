"""app URL Configuration

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
from django.urls import path,include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views



from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('data/<asal>',views.home,name="Data"),

    path('pendaftar_lulus/<nis>',views.lulus,name='lulus'),
    path('pendaftar_gagal/<nis>',views.gagal,name='gagal'),

    # List Sekolah
    path('list_sekolah/',views.index),
    path('list_sekolah/update/<npsn>',views.update),
    path('list_sekolah/delete/<npsn>',views.del_sekolah),
    path('list_sekolah/tambah',views.daftar),
    # End List Sekolah

    # List Pendaftar

    path('list_pendaftar/',views.list_pendaftar),
    path('list_pendaftar/tambah',views.tambah_pendaftar),
    path('list_pendaftar/update/<nis>',views.list_pendaftar),
    path('list_pendaftar/delete/<nis>',views.del_pendaftar),
    # End List Pendaftar
    path('logout/',auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout')

]