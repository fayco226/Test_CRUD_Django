from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .froms import TaskForm
# Create your views here.


def list_tasks(request):
    
    taks = Task.objects.all()
    return render(request, "list-tasks.html", {'tasks':taks})

def add_task(request):
    
    if request.method == "POST":
       # title = request.POST['title']
        #task = Task.objects.create(title = title)
        task = TaskForm(request.POST)
        task.save()
        return redirect('list_tasks')
    form = TaskForm()
    return render(request, "add-task.html",{'form':form})

def update_task(request, id):
    task_to_update = get_object_or_404(Task, pk=id)
    #task_to_update = Task.objects.filter(id=id)
    if request.method == "POST":
        # title = request.POST['title']
        # task_to_update.update(title=title)
        task = TaskForm(request.POST, instance=task_to_update )
        task.save()
        return redirect('list_tasks')
    form = TaskForm(instance=task_to_update )
    context = {
        'form':form
        }
    return render(request, "add-task.html",context)

def delete_task(request, id):
    
    task_to_delete= get_object_or_404(Task, pk=id)
    task_to_delete.delete()
    return redirect('list_tasks')
    