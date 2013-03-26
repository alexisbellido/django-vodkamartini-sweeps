from django.conf.urls.defaults import patterns, include, url
from .views import SweepEntryDetail, SweepEntrySubmitted

urlpatterns = patterns('vodkamartinisweeps.views',
    #url(r'^$', 'sweeps_index', {'page': 1}, name='vodkamartinisweeps_home'),
    #url(r'^page-(?P<page>\d+)/$', 'sweeps_index', name='vodkamartinisweeps_index'),
    #url(r'^(?P<slug>[-\w]+)/$', 'sweeps_detail', name='vodkamartinisweeps_sweep_detail'),
    url(r'^(?P<slug>[-\w]+)/$', SweepEntryDetail.as_view(), name='vodkamartinisweeps_sweepentry_detail'),
    # TODO thank you page after submitting SweepEntry
    #url(r'^(?P<slug>[-\w]+)/question/(?P<pk>\d+)/$', QuestionDetail.as_view(), name='vodkamartiniquiz_question_detail'),
    #url(r'^(?P<slug>[-\w]+)/result/$', QuizResultDetail.as_view(), name='vodkamartiniquiz_quizresult_detail'),
    #url(r'^(?P<slug>[-\w]+)/$', QuizDetail.as_view(), name='vodkamartiniquiz_quiz_detail'),
)
