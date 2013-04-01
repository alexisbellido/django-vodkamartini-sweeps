from django.conf.urls.defaults import patterns, include, url
from .views import SweepEntryDetail, SweepEntrySubmitted

urlpatterns = patterns('vodkamartinisweeps.views',
    url(r'^(?P<slug>[-\w]+)/$', SweepEntryDetail.as_view(), name='vodkamartinisweeps_sweepentry_detail'),
    url(r'^(?P<slug>[-\w]+)/entry/(?P<sweepentry_pk>\d+)/$', SweepEntrySubmitted.as_view(), name='vodkamartinisweeps_sweepentry_submitted'),
)
