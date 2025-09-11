from django.db import models

# Create your models here.
class Project(models.Model):
    author = models.ForeignKey("members.Profile", on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # genre = models.CharField(max_length=100, blank=True, null=True)
    project_format = models.ForeignKey('badges.Format', on_delete=models.SET_NULL, null=True, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # cover_image = models.URLField(blank=True, null=True) NTS: implement image upload with cloudinary
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Draft(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='drafts')
    version = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return f"Draft {self.version} for {self.project.name}"
    

class DraftBadge(models.Model):
    draft = models.ForeignKey(Draft, on_delete=models.CASCADE, related_name='badges')
    badge = models.ForeignKey('badges.Badge', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('draft', 'badge')
        verbose_name_plural = "draft badges"

    def __str__(self):
        return f"{self.badge_type} badge for {self.draft}"