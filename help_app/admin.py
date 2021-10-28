from django.contrib import admin

from . import models
from .models import Parents

# Register your models here.

#admin.site.register(Parents)

@admin.register(models.Parents)
class ParentsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Children)
class ChildrenAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tasks)
class TasksAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Houseworks)
class HouseworksAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Days_comment)
class Days_commentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


# Register your models here.