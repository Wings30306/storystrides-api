from django.contrib import admin
from .models import Badge, Category, BadgeCategory, Format

# Register your models here.
admin.site.register(Badge)
admin.site.register(Category)
admin.site.register(BadgeCategory)
admin.site.register(Format)
