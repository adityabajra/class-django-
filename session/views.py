from django.shortcuts import redirect, render
from .models import Student
from django.contrib.auth.hashers import check_password

# Create your views here.
def student_login(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)

        try:
            student=Student.objects.get(username=username)
            if check_password(password,student.password):
                request.session[student.id]=student.id
                request.session[student.name]=student.name
                return redirect('dashboard')
            else:
                return render(request,'session/login/index.html',{"error":"Invalid Password"})

        except:
            return render(request,'session/login/index.html',{"error":"Not Found"})

    return render(request,'session/login/index.html')

def student_dashboard(request):
    if 'student_id' not in request.session:
        return redirect('login')
     
    name= request.session.get('student_name')
    return render(request,"session/login/dashboard.html",{"name":name})

def student_logout(request):
    request.session.flush()
    return redirect('login')