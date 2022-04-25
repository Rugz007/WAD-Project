from django.contrib import admin

from .models import Language, Project, Sentence

# Register your models here.
@admin.register(Language)
class Languages(admin.ModelAdmin):
    list_display=['language_id','name']
@admin.register(Project)
class Projects(admin.ModelAdmin):
    list_display=['project_id','wiki_title']

admin.site.register(Sentence)