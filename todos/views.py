from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList
from todos.forms import TodoListForm

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


def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list_instance = form.save()
            return redirect("todo_list_detail", id=todo_list_instance.id)
    else:
        form = TodoListForm()
    context = {"form": form}
    return render(request, "todos/create.html", context)
