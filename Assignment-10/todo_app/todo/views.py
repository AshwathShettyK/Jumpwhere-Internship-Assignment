from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import TaskForm
from .models import Task


def task_list(request):
    search = request.GET.get("search", "")
    status = request.GET.get("status", "all")
    tasks = Task.objects.all()

    if search:
        tasks = tasks.filter(Q(title__icontains=search) | Q(description__icontains=search))

    if status == "completed":
        tasks = tasks.filter(completed=True)
    elif status == "pending":
        tasks = tasks.filter(completed=False)

    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(completed=True).count()
    pending_tasks = Task.objects.filter(completed=False).count()

    return render(request, "todo/home.html", {
        "tasks": tasks,
        "search": search,
        "status": status,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
    })


def task_add(request):
    form = TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("todo:home")
    return render(request, "todo/task_form.html", {"form": form, "title": "Add Task"})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("todo:detail", pk=task.pk)
    return render(request, "todo/task_form.html", {"form": form, "title": "Edit Task"})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "todo/task_detail.html", {"task": task})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("todo:home")
    return render(request, "todo/task_delete.html", {"task": task})


def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save(update_fields=["completed"])
    return redirect(request.META.get("HTTP_REFERER", "todo:home"))
