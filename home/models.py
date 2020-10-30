from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='covers')

    def __str__(self):
        return self.title

class Job(models.Model):
    position = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    employer = models.CharField(max_length=100)
    location = models.TextField(default=None)
    image = models.ImageField(upload_to='job_cover')
    badges = models.TextField(default=None)

    def __str__(self):
        return self.position

class Project(models.Model):
    title = models.CharField(max_length=50)
    project_type = models.CharField(max_length=75)
    decription = models.TextField(default=None)
    button_title = models.CharField(max_length=30)
    button_link = models.URLField()
    
    def __str__(self):
        return self.title