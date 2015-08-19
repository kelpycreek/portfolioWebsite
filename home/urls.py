from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pictureName>.*)/$', views.closeUp, name='pictureName'),
]
