from django.shortcuts import render , get_object_or_404 , redirect

# Create your views here.
from .models import Task


def home(request):
    tasks = Task.objects.filter(is_Completed=False).order_by('-created_at')
    
    context = {'tasks': tasks}
    
    return render(request, 'todo/home.html' , context)




def mark_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_Completed = True
    task.save()
    return redirect('todo:home')  # Replace 'task_list' with your list view name



def delete_task(request, task_id):
    task = get_object_or_404(Task,id=task_id)
    
    task.delete()
    return redirect('todo:home')

def add_task(request):
    if request.method == 'POST':
        task_text = request.POST.get('task')
        if task_text:
            Task.objects.create(task=task_text)
        return redirect('todo:home')  # change to your list view name

    return render(request, 'todo/add.html')  # template name