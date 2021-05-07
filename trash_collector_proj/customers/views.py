from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    print(user)
    return render(request, 'customers/index.html')


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        weekly_pickup = request.POST.get('weekly_pickup')
        one_time_pickup = request.POST.get('one_time_pickup')
        balance = request.POST.get('balance')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        new_customer = Customer(name=name, weekly_pickup=weekly_pickup, one_time_pickup=one_time_pickup, balance=balance, start_date=start_date, end_date=end_date, address=address, zip_code=zip_code)
        new_customer.save()
        return HttpResponseRedirect(reversed('customers:new_customer'))
    else:
        return render(request, '/home.html')
