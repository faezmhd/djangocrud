from django.shortcuts import render, redirect

# Create your views here.
from new_app.forms import TodoForm
from new_app.models import Todo


# def home(request):
#     return render(request, template_name='home.html')
def home2(request):
    return  render(request, template_name='home2.html')
def index(request):
    return render(request, template_name='index.html')


def todo(request):
    data = TodoForm()

    if request.method == 'POST':
        message = TodoForm(request.POST)
        if message.is_valid():
            message.save()
            return redirect('views_todo')

    return render(request,template_name='dashboard.html',context={'data':data})

def views_todo(request):
    data = Todo.objects.all()
    print(data)

    return render(request,template_name='views.html',context={'data':data})


def delete(request,id):
    data = Todo.objects.get(id=id)
    data.delete()
    return redirect('views_todo')

def update(request,id):

    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('views_todo')

    return render(request,'update.html',{'form':form})