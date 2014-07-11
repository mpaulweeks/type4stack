from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'type4stack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('', include('type4.urls', namespace="type4")),
    url(r'^admin/', include(admin.site.urls)),
)
