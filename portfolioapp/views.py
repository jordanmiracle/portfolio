from django.shortcuts import render
from .models import Project
from django.http import HttpResponse
from .models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, 'portfolioapp/index.html', {'projects': projects})


def project_detail(request):
    project = Project.objects.get(id=1)
    context = {
        'project': project
    }
    return render(request, 'portfolioapp/index.html/', context)


def frontend(request):
    return HttpResponse(render(request, 'portfolioapp/vue_index.html'))
