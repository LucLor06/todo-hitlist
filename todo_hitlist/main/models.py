from django.db import models
from django.contrib.auth.models import AbstractUser
from config.settings import STATIC_URL
from django.utils.text import slugify


class User(AbstractUser):
    ...

class TodoApp(models.Model):
    technology = models.CharField(max_length=32)
    slug = models.SlugField(blank=True, unique=True, editable=False)
    date = models.DateField(auto_now_add=True)
    github_link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.technology
    
    def save(self, *args, **kwargs):
        slug = slugify(self.technology)
        if self.slug != slug:
            self.slug = slug
        super().save(*args, **kwargs)
    
    def icon(self):
        return f'{STATIC_URL}icons/{self.slug}.png'
    
    def template(self):
        return f'todo_apps/{self.slug}/{self.slug}.html'