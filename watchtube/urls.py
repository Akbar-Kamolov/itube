from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('', views.create_video, name='create_video')
]