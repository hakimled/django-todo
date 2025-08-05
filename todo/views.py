from django.shortcuts import render , get_object_or_404 , redirect
from .models import Task
from .forms import TaskForm

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo:task_list')  # adjust as needed
    else:
        form = TaskForm(instance=task)

    return render(request, 'todo/edit_task.html', {'form': form})


def home(request):
    tasks = Task.objects.filter(is_Completed=False).order_by('-updated_at')
    
    context = {'tasks': tasks}
    
    return render(request, 'todo/homo.html' , context)




def mark_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_Completed = True
    task.save()
    return redirect('todo:task_list')  # Replace 'task_list' with your list view name



def delete_task(request, task_id):
    task = get_object_or_404(Task,id=task_id)
    
    task.delete()
    return redirect('todo:task_list')

def add_task(request):
    if request.method == 'POST':
        task_text = request.POST.get('task')
        if task_text:
            Task.objects.create(task=task_text)
        return redirect('todo:task_list')  # change to your list view name

    return render(request, 'todo/add.html')  # template name