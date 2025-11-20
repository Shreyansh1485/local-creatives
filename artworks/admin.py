from django.contrib import admin
from .models import Artwork, Tag
@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title','artist','created_at','featured')
    list_filter = ('featured','created_at')
    search_fields = ('title','description','artist__username')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(artist=request.user)
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
