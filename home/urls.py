from django.conf import settings
from django.urls import path, include

from .views import indexView

urlpatterns = [
    path('', indexView, name='home'),
]