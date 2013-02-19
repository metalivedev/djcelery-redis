from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django import forms
from celery.task.control import inspect

from minestrone.soup import tasks

class JobsView(TemplateView):
    template_name = 'soup/jobs.html'

    def get_context_data(self, **kwargs):
        return {
            'params': kwargs,
            'nodes': inspect().active(),
        }

class EditorView(FormView):

    class FormAddJob(forms.Form):
        job_name = forms.CharField(
                max_length=128,
                required=True,
                label='Job name:'
        )
        routing_key_name = forms.CharField(
                max_length=128,
                required=True,
                label='Routing key name:',
                initial='default'
        )

    template_name = 'soup/editor.html'
    success_url = '/jobs/'
    form_class = FormAddJob

    def form_valid(self, form):
        name = form.cleaned_data['job_name']
        routing_key = 'tasks.{0}'.format(form.cleaned_data['routing_key_name'])
        tasks.lazy_job.apply_async(args=[name], routing_key=routing_key)
        return HttpResponseRedirect(self.get_success_url())
