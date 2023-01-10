from django.shortcuts import render
from . models import Task,Fileupload,Comment
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
def index(request):
    return render(request,"todolist/index.html")
def datapost(request):
    tasid=request.POST.get('taskid')
    if (tasid==""):
      r=Task(task=request.POST.get("uid"))
      r.save()
    else:
        r=Task(task=request.POST.get("uid"),id=tasid)
        r.save()
        
    data=Task.objects.values()
    data1=list(data)
    return JsonResponse({"data1":data1} )

def fileupload(request):
    if request.method=="POST":
       myfile = request.FILES['fdata']
       title=request.POST['txttitle']
       detail=request.POST['txtdetail']
       fs = FileSystemStorage()
       fs.save(myfile.name,myfile)
       obj = Fileupload(filepath=myfile.name,title=title,detail=detail)
       obj.save()
       return render(request,"todolist/detail.html",{"res":Fileupload.objects.all()})
    return render(request,"todolist/fileupload.html")
def delete(request):
    if request.method=='POST':
        id=request.POST.get('sid')
        print(id)
        pi=Task.objects.get(pk=id)
        pi.delete()
        return JsonResponse({"status":'successfully deleted'})
# def delete(request):
#     if request.method == 'POST':
#         todo_name = request.POST.get('todo_name')
#         print(todo_name)
#         Task.objects.filter(task=todo_name).delete()
#         return JsonResponse({'status': "deleted","return":todo_name}) 
def edit(request):
     if request.method == "POST":
      id=request.POST.get('sid')
      task=Task.objects.get(pk=id)
      task_data={"id":task.id,'task':task.task}
      return JsonResponse(task_data)
def commentpost(request):
    if request.method=='POST':
       comment=request.POST.get('cid')
       print(comment)
       r=Comment(comment=comment)
       r.save()
       data=list(Comment.objects.values())
       return JsonResponse({'data1':data})

def detail(request):
    pass