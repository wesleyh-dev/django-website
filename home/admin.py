from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Job
from .models import Project

admin.site.register(Book)
admin.site.register(Job)
admin.site.register(Project)