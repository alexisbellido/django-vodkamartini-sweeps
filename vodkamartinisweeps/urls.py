from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('vodkamartinisweeps.views',
    url(r'^$', 'sweeps_index', {'page': 1}, name='vodkamartinisweeps_home'),
    url(r'^page-(?P<page>\d+)/$', 'sweeps_index', name='vodkamartinisweeps_index'),
    url(r'^(?P<slug>[-\w]+)/$', 'sweeps_detail', name='vodkamartinisweeps_detail'),
)
