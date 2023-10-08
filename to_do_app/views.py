from django.shortcuts import render
from todo_list.models import Task


def home(request):
    """ Home page"""
    tasks = Task.objects.filter(is_completed=False,).order_by('-updated_on')

    context = {
        'tasks': tasks,
    }
    return render(request, 'home.html', context)