from django.conf.urls import patterns, include, url
from django.contrib import admin
# from appLibro. import views

urlpatterns = patterns('appLibro.views',
    # Examples:
    # url(r'^$', 'appLibro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^hello/$', 'hello'),
    (r'^hora/$', 'hora_actual'),
    (r'^hora/mas/(\d{1,2})/$', 'horas_de_mas'),
    (r'^extra/$', 'muestra_META'),
    (r'^contacto/$', 'contacto'),
    (r'^busqueda/$', 'busqueda'),
    (r'^edad/(?P<nombre>[^/]+)/(?P<edad>\d+)/$', 'nombre'),

    #Si yo tubiera otras rutas podria hacer otra variable urlpatterns y sumarle la ruta
    #urlpatterns += patterns('weblog.views',
            # (r'^web/(\w)/$', 'post'),
        # )
)
