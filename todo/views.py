from django.shortcuts import render,redirect
from django.http import HttpRequest

from todo.models import Todo

# Create your views here.
#start comment
#def index(request):
 #   todo = Todo(title=request.GET.get("title"))

   # todo.save()
    #context = {
     #   "todos": Todo.objects.all()
    #}
    #return render(request,'index.html', context
    #end comment#}
    
def index(request):
  todo=Todo.objects.all()
  if request.method == 'POST':
    new_todo=Todo(title=request.POST['title'])
    new_todo.save()
    return redirect('/')
        
  return render(request,'index.html',{'todos':todo})

def delete(request,pk):
  del_todo=Todo.objects.get(id=pk)  
  del_todo.delete()

  return redirect('/')