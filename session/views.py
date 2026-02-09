from django.shortcuts import render

def student_login(request):
    return render(request, 'session/login/index.html')
def student_dashboard(request):
    return render(request, 'session/login/dashboard.html')
def student_logout(request):
    pass
