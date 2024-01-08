from django.shortcuts import render,redirect
from studentapp.models import course
from studentapp.models import student

# Create 
# your views here.
def index(request):
    return render(request,'index.html')
def addcourse(request):
    return render(request,'course.html')
def add_course(request):
    if request.method=='POST':
        c=request.POST.get('coursename')
        f=request.POST.get('fees')
        ck=course(course_name=c,fee=f)
        ck.save()
        return redirect('/')
def add_student(request):
    courses=course.objects.all()
    return render(request,'student.html',{'coursekey':courses})
def add_studentdetails(request):
    if request.method=='POST':
        studentname=request.POST['name']
        studentaddress=request.POST['address']
        studentage=request.POST['age']
        studentdate=request.POST['joiningdate']
        studentcourse=request.POST['sel']
        course1=course.objects.get(id=studentcourse)
        s=student(student_name=studentname,student_address=studentaddress,student_age=studentage,joining_date=studentdate,cours=course1)
        s.save()
        return redirect('/')
def show_details(request):
    s=student.objects.all()
    return render(request,'show_details.html',{'skey':s})
def edit(request,pk):
    s=student.objects.get(id=pk)
    c=course.objects.all()
    return render(request,'edit.html',{'stud':s,'ckey':c})
def edit_studentdetails(request,pk):
    if request.method=='POST':
        s=student.objects.get(id=pk)
        s.student_name=request.POST['name']
        s.student_address=request.POST['address']
        s.student_age=request.POST['age']
        s.joining_date=request.POST['joiningdate']
        se=request.POST['sel']
        course1=course.objects.get(id=se)
        s.cours=course1
        s.save()
        return redirect('show_details')
    return render(request,'edit.html')
def delete1(request,pk):
    p=student.objects.get(id=pk)
    p.delete()
   
    return redirect('show_details')