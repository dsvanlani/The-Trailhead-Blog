from django.db import models

# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    content = models.FileField(upload_to='articles/')
    description = models.TextField()
    url = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=64, null=False)
    author_email = models.CharField(max_length=64, null=False)
    body = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

class Subscriber(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    subscriber_id = models.CharField(max_length=16)
    active = models.BooleanField(default=True)

