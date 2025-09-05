from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.username