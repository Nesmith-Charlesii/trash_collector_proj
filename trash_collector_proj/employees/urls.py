from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('employee_form/', views.employee_form, name='employee_form'),
    path('create_employee_profile/', views.create_employee_profile, name='create_employee_profile'),
    path('employee_profile/<int:employee_id>/', views.employee_profile, name='employee_profile')
]
