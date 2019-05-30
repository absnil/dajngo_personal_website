from django.shortcuts import render
from .models import Project
# Create your views here.

def project_list(request):
	project=Project.objects.order_by('date')
	return render(request,'projects/projects.html', {'project': project})
