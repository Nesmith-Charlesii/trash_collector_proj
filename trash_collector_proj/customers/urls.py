from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('customer_form/', views.customer_form, name='customer_form'),
    path('create_profile/', views.create, name='create'),
    path('customer_profile/<int:customer_id>/', views.customer_profile, name='customer_profile'),
    path('customer_profile/change_pickup/<int:customer_id>', views.change_pickup, name='change_pickup')
]
