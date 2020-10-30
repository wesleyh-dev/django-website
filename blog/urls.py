from django.conf import settings
from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.indexView, name='blog'),
    path('<int:post_id>/', views.detailView, name='detail')
]