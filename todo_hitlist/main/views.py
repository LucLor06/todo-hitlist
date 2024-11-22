from django.shortcuts import render
from .models import TodoApp
from django.views.generic import DetailView


def home(request):
    return render(request, 'home.html')


class TodoAppDetailView(DetailView):
    model = TodoApp
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    template_name = 'todo_apps/todo-app.html'
    context_object_name = 'todo_app'