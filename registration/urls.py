from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('',views.list_user, name='home'),
    # path('form/',views.registration_form, name='form'),
    path('form/',views.registration_form_sql_injection, name='form'),
]
