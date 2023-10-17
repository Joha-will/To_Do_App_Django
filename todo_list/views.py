from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from . models import Task


def add_task(request):
    """ This view gives users the ability to add tasks """
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def mark_as_done(request, pk):
    """ This view gives users the ability mark tasks as done """

    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def mark_as_undone(request, pk):
    """ This view gives users the ability undo tasks """

    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


def edit_task(request, pk):
    """ This view gives users the ability edit tasks """

    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')

    else:
        context = {
            'get_task': get_task,
        }
    return render(request, 'edit_task.html', context)


def delete_task(request, pk):
    """ This view gives users the ability delete tasks """

    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')