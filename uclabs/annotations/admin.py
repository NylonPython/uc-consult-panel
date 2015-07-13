from django.contrib import admin
from . import models

# Register your models here.

class AnnotationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'supervisor', 'ann_type', 'ann_text')

admin.site.register(models.Annotation, AnnotationAdmin)
