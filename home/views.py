from django.shortcuts import render

from .models import Book
from .models import Job
from .models import Project

# Create your views here.
def indexView(request):
    books = Book.objects.all()
    jobs = Job.objects.all()
    projects = Project.objects.all()

    template = 'home/index.html'
    context = {
        'books': books, 
        'jobs': jobs, 
        'projects': projects
    }
    
    return render(
        request, 
        template, 
        context
    )

