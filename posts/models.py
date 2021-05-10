from django.contrib.auth.models import User
from django.db import models

from authentication.models import Profile


class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
