from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'title'
    
    def get_queryset(self):
        """ return the title """
        return u'%s' % ('index')
    
# Create your views here.
