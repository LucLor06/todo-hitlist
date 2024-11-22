from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TodoApp
from pathlib import Path

@receiver(post_save, sender=TodoApp)
def todo_app_created(sender, instance, created, **kwargs):
    if created:
        todo_apps = Path(__file__).parent / 'templates' / 'todo_apps'
        todo_app_dir = todo_apps / instance.slug
        todo_app_dir.mkdir(parents=True, exist_ok=True)
        
        todo_app_template = todo_app_dir / f'{instance.slug}.html'
        todo_app_template.write_text('Edit me!')