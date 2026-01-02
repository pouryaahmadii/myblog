from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='articles')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    short_description = models.CharField(max_length=500, blank=True)
    date = models.DateField(auto_now_add=True)

    def short_body(self):
        return self.body[:300]

    def save(self, *args, **kwargs):
        save = super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title)
        return save

    def __str__(self):
        return f"{self.author} / {self.title}"
