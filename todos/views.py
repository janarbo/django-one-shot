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


def todo_list_update(request, id):
    todo_list_item = TodoList.objects.get(id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo_list_item)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoListForm(instance=todo_list_item)

    context = {"todo_list_item": todo_list_item, "form": form}

    return render(request, "todos/edit.html", context)


def todo_list_delete(request, id):
    delete_item = TodoList.objects.get(id=id)
    if request.method == "POST":
        delete_item.delete()
        return redirect("todo_list_list")

    return render(request, "todos/delete.html")
