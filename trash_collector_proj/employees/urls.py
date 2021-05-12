from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('employee_form/', views.employee_form, name='employee_form'),
    path('create_employee_profile/', views.create_employee_profile, name='create_employee_profile'),
    path('employee_profile/<int:employee_id>/', views.employee_profile, name='employee_profile'),
    path('employee_prospects/<int:employee_id>', views.employee_prospects, name='employee_prospects'),
    path('employee_prospect_search/<int:employee_id>/', views.prospect_search, name='prospect_search'),
    path('employee_prospect/results/<str:form_input>/<int:employee_id>/', views.employee_prospect_results, name='employee_prospect_results'),
    path('confirm_pickup/one_time/<int:employee_id>/<int:customer_id>/', views.confirm_one_time, name='confirm_one_time'),
    path('confirm_pickup/weekly/<int:employee_id>/<int:customer_id>/', views.confirm_weekly, name='confirm_weekly')
]
