from django.conf.urls import patterns, url

from type4 import views, admin_views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.all_cards, name='all_cards'),
    url(r'^filter/$', views.filter, name='filter'),
    url(r'^changes/$', views.changes, name='changes'),
    url(r'^admin/add_cards/$', admin_views.add_cards, name='admin_add_cards'),
    url(r'^admin/update/$', admin_views.update, name='admin_update'),
)