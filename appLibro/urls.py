from django.conf.urls import patterns, include, url
from django.contrib import admin
from appLibro.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'appLibro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^hora/$', hora_actual),
    (r'^hora/mas/(\d{1,2})/$',horas_de_mas),
    ('^extra/$', muestra_META),
    ('^contacto/$', contacto),
    ('^busqueda/$', busqueda),
)
