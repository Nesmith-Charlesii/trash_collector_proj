from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Customer


# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    print(user)
    customers = Customer.objects.all()
    for customer in customers:
        if user.id == customer.user.id:
            print(f'This user has a customer account')
            print(f'customer ID is {customer.id}')
            return HttpResponseRedirect(f'customer_profile/{customer.id}')
        else:
            print('This user has no customer profile')
    return HttpResponseRedirect(reverse('customers:customer_form'))


def customer_form(request):
    return render(request, 'customers/customer.html')


def create(request):
    user_id = request.user
    print(user_id.id)
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zipcode')
        user_id = user_id
        new_customer = Customer(name=name, address=address,
                                zipcode=zip_code, balance=0, user=user_id)
        new_customer.save()
        return HttpResponseRedirect(f'/customers/customer_profile/{new_customer.id}')
    else:
        return render(request, '/customer.html')


def customer_profile(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    context = {
        'customer': customer
    }
    return render(request, 'customers/customer_profile.html', context)


def change_pickup(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    context = {
        'customer': customer
    }
    return render(request, 'customers/change_pickup.html', context)


def update_weekly_pickup(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    change_weekly_pickup = request.POST.get('update_weekly_pickup')
    customer.weekly_pickup = change_weekly_pickup
    customer.save()
    # include '/' before redirect
    return HttpResponseRedirect(f'/customers/customer_profile/{customer.id}')


def one_time_pickup(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    customer.one_time_pickup = request.POST.get('one_time_pickup')
    customer.save()
    return HttpResponseRedirect(f'/customers/customer_profile/{customer.id}')


