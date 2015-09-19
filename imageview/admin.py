from django.contrib import admin
from .models import Image
from taggit_helpers import TaggitListFilter


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)
    list_filter = [TaggitListFilter]

admin.site.register(Image, ImageAdmin)
