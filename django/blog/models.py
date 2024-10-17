import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.date_posted >= timezone.now() - datetime.timedelta(days=1)