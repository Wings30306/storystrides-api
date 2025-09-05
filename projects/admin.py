from django.contrib import admin
from .models import Project, Draft, DraftBadge
# Register your models here.
admin.site.register(Project)
admin.site.register(Draft)
admin.site.register(DraftBadge)
