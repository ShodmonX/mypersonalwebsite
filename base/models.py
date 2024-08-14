from django.db import models 
from django.contrib.auth.models import  AbstractUser
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    image = models.ImageField(upload_to='img')

    url = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None)
    body = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)


    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.first_name