# urls.py

urlpatterns = [
    path('', views.TaskListView.as_view(), name='tasks'),
    path('create/', views.TaskCreateView.as_view(), name='tasks-create'),
    path('&lt;pk&gt;/delete/', views.TaskDeleteView.as_view(), name='tasks-delete')
]