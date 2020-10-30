from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title
