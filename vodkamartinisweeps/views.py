from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin

from .models import Sweep, SweepEntry
from .forms import SweepEntryForm


def sweeps_index(request, page=1):
    """
    Explain the purpose of this view.
    """

    # do something
    return render(request, 
                  'vodkamartinisweeps/sweeps_list.html',
                  {
                    'var': 'this is a variable',
                  },
                  )

def sweeps_detail(request, slug):
    output = "Test slug: %s" % (slug,)
    return HttpResponse(output)

class SweepEntryDetail(FormView, SingleObjectMixin):
    """
    Display the form to enter the sweeps by creating a SweepEntry instance.
    """

    form_class = SweepEntryForm
    template_name = 'vodkamartinisweeps/sweepentry_form.html'
    queryset = Sweep.live.all()

    def get_initial(self):
        self.sweep = self.get_object()
        #self.pk = self.object.pk
        #self.num_questions = len(self.question_pk_list)
        #return {'question': self.object, 
        #        'user': self.request.user,
        #        'num_questions': self.num_questions,
        #        'previous_question_id': self.previous_question_id,
        #       }

    #def redirect_previous_question(self):
    #    return HttpResponseRedirect(reverse('vodkamartiniquiz_question_detail', 
    #                                            kwargs={'slug': self.object.quiz.slug, 'pk': self.previous_question_id}
    #                                   ))

    #def form_valid(self, form):
    #    #messages.info(self.request, 'Question answered.')
    #    if 'previous_question' in self.request.POST:
    #        return self.redirect_previous_question()
    #    if 'next_question' in self.request.POST:
    #        self.success_url = form.save()
    #        return super(QuestionDetail, self).form_valid(form)

    #def form_invalid(self, form):
    #    #messages.info(self.request, 'Submission problem, please try again.')
    #    if 'previous_question' in self.request.POST:
    #        return self.redirect_previous_question()
    #    return super(QuestionDetail, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        """
        Populate the context.
        Most of these details are initialized on self.get_initial
        """
        context = super(SweepEntryDetail, self).get_context_data(**kwargs)
        context['sweep'] = self.sweep
        context['sweep_slug'] = self.sweep.slug
        return context

class SweepEntrySubmitted(DetailView):
    queryset = Sweep.live.all()
