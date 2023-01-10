from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Faculty,Student,Course,Teacher
from django.db.models import Avg
def teacher(request):
    if request.method=='POST':
        obj=Teacher(name=request.POST['textname'],email=request.POST['textemail'],password=request.POST['textpass'])
        obj.save()
    return render(request,'review/index.html')
def login(request):
    if request.method=='POST':
        check=Teacher.objects.get(name=request.POST['textname'],password=request.POST['textpass'])
        request.session["login1"]=request.POST["textname"]
        if (check>0):
            if request.session.has_key("login1"):

            

                data2=Faculty.objects.filter(name=request.session['login1'])
                data1=Student.objects.filter(faculty__name=request.session["login1"])
                python=Student.objects.filter(faculty__name=request.session["login1"],course1=1).aggregate(Avg('rating'))
                java=Student.objects.filter(faculty__name=request.session["login1"],course1=2).aggregate(Avg('rating'))
                javascript=Student.objects.filter(faculty__name=request.session["login1"],course1=3).aggregate(Avg('rating'))
                css=Student.objects.filter(faculty__name=request.session["login1"],course1=4).aggregate(Avg('rating'))
                data=Student.objects.filter(faculty__name=request.session["login1"]).aggregate(Avg('rating'))
                datafloat=str("%.1f"%data.get('rating__avg'))
                if type(python.get('rating__avg'))== int or type(python.get('rating__avg'))== float:
                    python=str("%.1f"%python.get('rating__avg'))
                else:
                    python=str(python.get('rating__avg'))
                if type(javascript.get('rating__avg'))== int or type(javascript.get('rating__avg'))== float:
                    javascript=str("%.1f"%javascript.get('rating__avg'))
                else:
                    javascript=str(javascript.get('rating__avg'))
                if type(java.get('rating__avg'))== int or type(java.get('rating__avg'))== float :
                    java=str("%.1f"%java.get('rating__avg'))
                else:
                    java=str(java.get('rating__avg'))
                if type(css.get('rating__avg'))== int or type(css.get('rating__avg'))== float:
                    css=str("%.1f"%css.get('rating__avg'))
                else:
                    css=str(css.get('rating__avg'))     
                return render(request,'review/detail.html',{"key":datafloat,"key1":data1,"key2":data2,"python":python,'javascript':javascript,'java':java,'css':css}
                )
            else:
                return redirect('/review')
def logout(request):
    del request.session["login1"]
    return redirect("/review")

def course(request):
    data=Course.objects.all()
    return render(request,'review/course.html',{"key":data})

def faculty(request):
    data=Faculty.objects.filter(id=request.GET['q'])
    return render(request,'review/teacher.html',{"key":data})

def student(request):
    data=Student.objects.filter(id=request.GET['q'])
    return render(request,'review/student.html',{"key":data})
