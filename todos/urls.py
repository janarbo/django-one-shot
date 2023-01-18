from todos.views import todo_list_list
from django.urls import path


urlpatterns = [
    path("", todo_list_list, name="todo_list_list"),
]
