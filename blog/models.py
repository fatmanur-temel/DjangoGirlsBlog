from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    Create_date=models.DateTimeField(
        default=timezone.now)
    published_date=models.DateTimeField(
        blank=True, null=True)
    
    def published(self):
        self.published_date=timezone.now()
        self.save()
    
    def __str_(self):
        return self.title
    
    
    