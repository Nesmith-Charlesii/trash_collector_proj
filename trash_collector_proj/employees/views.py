from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .models import Employee

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    user = request.user
    print(user)
    return HttpResponseRedirect(f'/employees/employee_form')
    # return render(request, 'employees/index.html')


def employee_form(request):
    return render(request, 'employees/employee.html')


def create_employee_profile(request):
    user = request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        user_id = user
        new_employee = Employee(name=name, route_zipcode=zip_code, user=user_id)
        new_employee.save()
        return HttpResponseRedirect(f'/employees/employee_profile/{new_employee.id}')
    else:
        return HttpResponseRedirect('/employees/employee_form')


def employee_profile(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    context = {
        'employee': employee
    }
    return render(request, 'employees/employee_profile.html', context)
