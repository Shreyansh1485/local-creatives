from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Artwork
from .forms import ArtworkForm
def artwork_list(request):
    artworks = Artwork.objects.select_related('artist').prefetch_related('tags').order_by('-featured','-created_at')[:50]
    return render(request, 'artworks/artwork_list.html', {'artworks': artworks})
def artwork_detail(request, pk):
    art = get_object_or_404(Artwork, pk=pk)
    return render(request, 'artworks/artwork_detail.html', {'artwork': art})
@login_required
def artwork_create(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist = request.user
            artwork.save()
            form.save_m2m()
            return redirect('artwork_detail', pk=artwork.pk)
    else:
        form = ArtworkForm()
    return render(request, 'artworks/artwork_form.html', {'form': form})
@login_required
def artwork_delete(request, pk):
    art = get_object_or_404(Artwork, pk=pk)
    if art.artist != request.user:
        return HttpResponseForbidden("You are not allowed to delete this artwork.")
    if request.method == 'POST':
        try:
            art.image.delete(save=False)
        except Exception:
            pass
        art.delete()
        return redirect('artwork_list')
    return render(request, 'artworks/artwork_confirm_delete.html', {'artwork': art})
@login_required
def my_artworks(request):
    artworks = request.user.artworks.all().order_by('-created_at')
    return render(request, 'artworks/my_artworks.html', {'artworks': artworks})
