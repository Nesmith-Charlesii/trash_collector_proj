import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.apps import apps
from .models import Employee
from datetime import date

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    user = request.user
    print(user)
    all_employees = Employee.objects.all()
    for employee in all_employees:
        if user.id == employee.user_id:
            return HttpResponseRedirect(f'/employees/employee_profile/{employee.id}')
    return HttpResponseRedirect(reverse('employees:employee_form'))


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
    customers = apps.get_model('customers.Customer')
    all_customers = customers.objects.all()
    today = date.today()
    day = date.today().strftime("%A")
    context = {
        'employee': employee,
        'customers': all_customers,
        'date': today,
        'day': day
    }
    return render(request, 'employees/employee_profile.html', context)


def employee_prospects(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    customer = apps.get_model('customers.Customer')
    all_customers = customer.objects.all()
    context = {
        'employee': employee,
        'customers': all_customers
    }
    return render(request, 'employees/employee_prospects.html', context)


def prospect_search(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        form_input = request.POST.get('pickup_day')
        return HttpResponseRedirect(f'/employees/employee_prospect/results/{form_input}/{employee.id}')


def employee_prospect_results(request, form_input, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    Customer = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    pickup_day = form_input
    prospects = Customer.objects.filter(weekly_pickup=pickup_day)
    context = {
        'employee': employee,
        'customers': customers,
        'prospects': prospects
    }
    print(pickup_day)
    print(customers)
    return render(request, 'employees/employee_prospect_results.html', context)


def confirm_one_time(request, customer_id, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    Customer = apps.get_model('customers.Customer')
    target_customer = Customer.objects.get(pk=customer_id)
    target_customer.one_time_pickup = None
    target_customer.balance += 10
    target_customer.save()
    return redirect(f'/employees/employee_profile/{employee.id}')


def confirm_weekly(request, customer_id, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    Customer = apps.get_model('customers.Customer')
    target_customer = Customer.objects.get(pk=customer_id)
    target_customer.weekly_pickup = None
    target_customer.balance += 10
    target_customer.save()
    return redirect(f'/employees/employee_profile/{employee.id}')
