from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post_pics', default='default-image.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class FirstPageNews(models.Model):
    title = models.CharField(max_length=100)
    quote = models.TextField()
    image = models.ImageField(upload_to='first_page_pics', default='default-image.png')

    def __str__(self):
        return self.title