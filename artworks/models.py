from django.db import models
from django.conf import settings
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self): return self.name
class Artwork(models.Model):
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='artworks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='artworks/')
    tags = models.ManyToManyField(Tag, blank=True, related_name='artworks')
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    def __str__(self): return self.title
