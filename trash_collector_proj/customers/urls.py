from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('customer_form/', views.customer_form, name='customer_form'),
    path('create_profile/', views.create, name='create'),
    path('customer_profile/', views.customer_profile, name='customer_profile')
]
