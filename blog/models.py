from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
from django.utils.text import slugify

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='articles')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, allow_unicode=True, null=True)
    head_content = models.TextField(blank=True)
    body = models.TextField()
    foot_content = models.TextField(blank=True)
    short_description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField(auto_now_add=True)

    def short_body(self):
        return self.body[:300]
    def short_foot(self):
        return self.foot_content[:300]
    def short_head(self):
        return self.head_content[:300]

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title,allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.author} / {self.title}"
