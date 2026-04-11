from django.contrib import admin # pyright: ignore[reportMissingModuleSource]
from .models import Review  

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'stars', 'comment')