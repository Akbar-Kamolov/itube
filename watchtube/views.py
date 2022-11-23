from django.shortcuts import render, redirect
from .models import Video
from . import forms


def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {'videos': videos})


def create_video(request):
    if request.method == 'POST':
        form = forms.VideoForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect('iteration:videos')
    form = forms.VideosForm()
    return render(request, 'create_video.html', {'form': form})
