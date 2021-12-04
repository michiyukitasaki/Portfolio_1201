from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ContactForm
from .models import Profile, Work, Software, Technical
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
import textwrap
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm

# Create your views here.



class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by("-id")[0]
        work_data = Work.objects.order_by("-id")
        return render(request, 'app/index.html', {
            'profile_data': profile_data,
            'work_data': work_data
        })

class DetailView(View):
    def get(self, request, *args, **kwargs):
        work_data = Work.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/detail.html', {
            'work_data': work_data
        })

class AboutView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        software_data = Software.objects.order_by('-id')
        technical_data = Technical.objects.order_by('-id')
        return render(request, 'app/about.html',{
            'profile_data':profile_data,
            'software_data' : software_data,
            'technical_data' : technical_data  
        })


class ContactFormView(FormView):
    template_name = 'app/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_result')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ContactResultView(TemplateView):
    template_name = 'app/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context