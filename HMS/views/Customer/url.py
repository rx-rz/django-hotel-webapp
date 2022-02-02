from django.urls import path
from HMS.views.Customer import customer_view

urlpatterns = [
    path('register', customer_view.create_customer, name='register'),
    path('list_customers', customer_view.list_customer_if_post_method, name='list_customers'),
    path('list_customers_by_a_particular_term', customer_view.list_customer_by_a_particular_term,
         name='list_customers_by_a_particular_term'),
    path('customer_details', customer_view.get_customer_details, name='get_customer_details')
]
