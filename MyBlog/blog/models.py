from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField  # Import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=45)
    content = HTMLField()
    date_posted = models.DateTimeField(default=timezone.now)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
