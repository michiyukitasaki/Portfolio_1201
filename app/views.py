from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from .models import Profile, Work, Experience, Education

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
        experience_data = Experience.objects.order_by('-id')[0]
        education_data = Education.objects.order_by('-id')[0]
        return render(request, 'app/about.html',{
            'profile_data':profile_data,
            'experience_data':experience_data,
            'education_data':education_data,
        })