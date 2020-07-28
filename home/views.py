from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Book
from .models import Job
from .models import Project

# Create your views here.
def indexView(request):
    template = 'home/index.html'
    books = Book.objects.all()
    jobs = Job.objects.all()
    projects = Project.objects.all()
    
    return render(
        request, 
        template, 
        {
            'books': books, 
            'jobs': jobs, 
            'projects': projects
        }
    )

