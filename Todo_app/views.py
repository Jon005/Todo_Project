from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from Todo_app.models import Todo

def index(request):
    todo_items=Todo.objects.all().order_by("-added_date")
    return render(request,'index.html',{'todo_items':todo_items})

@csrf_exempt
def add_todo(request):
    #accept user input
    print(request.POST)
    current_date=timezone.now()
    content=request.POST["content"]
    #print(current_date)
    #print(content)
    #store userinput in database
    Todo.objects.create(added_date=current_date,text=content)
    return HttpResponseRedirect('/')

@csrf_exempt
def delete_todo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')




