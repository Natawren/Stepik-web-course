from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.test, name='index'),
    url(r'^login/.*$', views.test, name = 'login').
    url(r'^signup/.*$', view.test, name = 'signup'),
    url(r'^ask/.*$', view.test, name = 'ask'),
    url(r'^popular/.*$', view.test, name = 'popular'),
    url(r'^new/.*$', view.test, name = 'new'),
    url(r'^question/(?P<id>\d+)/$', view.test, name = 'question'),
    
]
