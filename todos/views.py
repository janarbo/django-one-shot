from django.shortcuts import render, get_object_or_404
from todos.models import TodoList

# Create your views here.


def todo_list_list(request):
    list = TodoList.objects.all()
    context = {"todo_list": list}
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    detail = TodoList.objects.get(id=id)
    context = {
        "todo_list_detail": detail,
    }
    return render(request, "todos/detail.html", context)
