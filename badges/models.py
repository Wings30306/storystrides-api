from django.db import models

# Create your models here.
class Badge(models.Model):
    short_name = models.CharField(max_length=100) # Must match image file name
    full_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    
class BadgeCategory(models.Model):
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, related_name='categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='badges')

    class Meta:
        unique_together = ('badge', 'category')
        verbose_name_plural = "badge categories"

    def __str__(self):
        return f"{self.badge.full_name} in {self.category.name}"
    
class Format(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='formats')

    def __str__(self):
        return self.name