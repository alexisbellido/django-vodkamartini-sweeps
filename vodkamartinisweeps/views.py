from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin

#from .models import Sweep, SweepEntry
#from .forms import SweepForm


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
