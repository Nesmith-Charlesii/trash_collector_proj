from django.urls import path
from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('customer_form/', views.customer_form, name='customer_form'),
    path('create_profile/', views.create, name='create'),
    path('customer_profile/<int:customer_id>/', views.customer_profile, name='customer_profile'),
    path('customer_profile/change_pickup/<int:customer_id>', views.change_pickup, name='change_pickup'),
    path('update_weekly_pickup/<int:customer_id>', views.update_weekly_pickup, name='update_weekly_pickup'),
    path('one_time_pickup/<int:customer_id>', views.one_time_pickup, name='one_time_pickup'),
    path('account_period/<int:customer_id>', views.account_period, name='account_period'),
    path('suspend_account/<int:customer_id>', views.suspend_account, name='suspend_account')
]
