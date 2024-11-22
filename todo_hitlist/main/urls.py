from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo-apps/<slug>/', views.TodoAppDetailView.as_view(), name='todo-app'),
]