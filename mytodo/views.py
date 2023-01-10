from django.shortcuts import render
from django.http import JsonResponse
from .models import TODO


def home(request):
    return render(request, 'mytodo/todo.html')

def todo_list(request):
    todos = TODO.objects.all()
    return JsonResponse({'todos': list(todos.values())})

def todo_create(request):
    if request.method == 'POST':
        todo_name = request.POST.get('todo_name')
        todo = TODO.objects.filter(name=todo_name)

        # we need to make sure that this todo does not exist in the database
        if todo.exists():
            return JsonResponse({'status': 'error'})

        todo = TODO.objects.create(name=todo_name)
        return JsonResponse({'todo_name': todo.name, 'status': 'created'})  