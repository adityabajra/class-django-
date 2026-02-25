from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration
from django.contrib.auth.hashers import make_password
from django.db import connection

def list_user(request):
    users = Registration.objects.all()
    user_input = "<script>alert(`You are hacked. Stealing cookies. ${document.cookie}`);</script>"
    return render(request, 'registration/index.html', {'users': users , 
                                                       "user_input": user_input})

@csrf_exempt
def registration_form_sql_injection(request):
    """Handle registration form display and submission"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # Get cleaned data
            data = form.cleaned_data
            hashPass = make_password(data['password'])
            
            sql = f"""
                INSERT INTO registration_registration (name, email, password)
                VALUES ('{data['name']}', '{data['email']}', '{hashPass}');
                """
            
            with connection.cursor() as cursor:
                cursor.executescript(sql)
            print("success")
            return render(request, 'registration/form.html',
                          {
                              'form':RegistrationForm(),
                              "success":"Successful"
                          })
    else:
        form = RegistrationForm()

    return render(request, 'registration/form.html', {'form': form})



def registration_form(request):
    """Handle registration form display and submission"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # Get cleaned data
            data = form.cleaned_data
            hashPass = make_password(data['password'])
            registration = Registration(
                name=data['name'],
                email=data['email'],
                password=hashPass,  
            )
            registration.save()
            print("success")
            return render(request, 'registration/form.html',
                          {
                              'form':RegistrationForm(),
                              "success":"Successful"
                          })
    else:
        form = RegistrationForm()

    return render(request, 'registration/form.html', {'form': form})