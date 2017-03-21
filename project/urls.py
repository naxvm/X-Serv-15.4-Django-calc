from django.conf.urls import include, url
from django.contrib import admin

from calc import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.default_response),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(\d+)\+(\d+)$', views.suma),
    url(r'^(\d+)\-(\d+)$', views.resta),
    url(r'^(\d+)\*(\d+)$', views.multiplicacion),
    url(r'^(\d+)\/(\d+)$', views.division),
    url(r'', views.not_found),  # por defecto, para cazar otras posibilidades
]
