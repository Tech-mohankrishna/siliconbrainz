from django.contrib import admin
from .models import pictures, PicturesCategory, PicturesSeries
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class picturesAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["pictures_title", "pictures_published"]}),
        ("URL", {"fields": ["pictures_slug"]}),
        ("Series", {"fields": ["pictures_series"]}),
        ("content", {"fields": ["pictures_content"]}),
        ("thumb", {"fields": ["pictures_thumb"]})   
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}

    }
admin.site.register(PicturesCategory)
admin.site.register(PicturesSeries)
admin.site.register(pictures, picturesAdmin)