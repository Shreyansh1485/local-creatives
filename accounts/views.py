from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import SignUpForm
from .models import Profile
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.get_or_create(user=user)
            login(request, user)
            return redirect('my_artworks')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'accounts/profile_detail.html', {'profile': profile})
@login_required
def profile_share(request):
    profile = request.user.profile
    url = request.build_absolute_uri(reverse('profile_detail', args=[profile.pk]))
    return render(request, 'accounts/profile_share.html', {'share_url': url})
