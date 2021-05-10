from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.apps import apps
from .models import Employee

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    user = request.user
    employees = Employee.objects.all()
    for employee in employees:
        if employee.id == user.id:
            return render(request, 'employees/index.html')
        else:
            return render(request, 'employees/employee_form.html')

def create(request):
    Customer = apps.get_model('customers.Customer')
    if request.method == 'POST':
        name = request.POST.get('name')
        route_zipcode = request.POST.get('route_zipcode')
        new_employee = Employee(name=name, route_zipcode=route_zipcode)
        new_employee.save()
        return render(request, 'employees/index.html')
