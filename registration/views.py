from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration


def registration_form(request):
    """Handle registration form display and submission"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # Get cleaned data
            print("success")
            return render(request, 'registration/form.html',
                          {
                              'form':form,
                              "success":"Successful"
                          })
    else:
        form = RegistrationForm()

    return render(request, 'registration/form.html', {'form': form})