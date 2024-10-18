import datetime

from django.db import models
from django.utils import timezone

from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = CKEditor5Field('Text', config_name='extends')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.date_posted >= timezone.now() - datetime.timedelta(days=1)