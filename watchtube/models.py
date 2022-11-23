from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField()
    video = models.FileField(blank=True)
    preview = models.ImageField(blank=True)
    description = models.TextField()