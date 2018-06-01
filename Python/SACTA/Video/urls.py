from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout_then_login
from SACTA import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index, name = "index"),
    url(r'^vigilancia/$', views.vigilancia, name = "vigilancia"),
    url(r'^login/$', login, {'template_name': 'login.html'}, name = 'login'),
    url(r'^logout/$', logout_then_login, name = 'logut'),
    url(r'^signup/$', views.SignUp.as_view(), name = 'signup'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
