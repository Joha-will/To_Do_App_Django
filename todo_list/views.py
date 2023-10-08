from django.shortcuts import render, redirect
from . models import Task


def add_task(request):
    """ This view gives users the ability to at tasks """
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
