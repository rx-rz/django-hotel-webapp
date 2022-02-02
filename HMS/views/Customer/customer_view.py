from django.http import HttpRequest
from django.shortcuts import redirect, render

from HMS.service_provider import hotel_service_provider
from HMS.dto.CustomerDto import RegisterCustomer


def create_customer(request):
    context = {
        'title': 'Register'
    }

    __create_customer_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('home')
    return render(request, 'customer/register.html', context)


def __get_attribute_from_request(request: HttpRequest):
    make_customer = RegisterCustomer()
    make_customer.first_name = request.POST['first_name']
    make_customer.last_name = request.POST['last_name']
    make_customer.email = request.POST['email']
    make_customer.password = request.POST['password']
    make_customer.phone_number = request.POST['phone_number']
    make_customer.confirm_password = request.POST['confirm_password']
    make_customer.date_of_birth = request.POST['date_of_birth']
    make_customer.username = request.POST['username']

    return make_customer
# def patient_details(request, patient_id: int):
#     patient = hms_service_provider.patient_management_service().patient_details(patient_id)
#     context = {
#         'patient': patient
#     }
#     return render(request, 'Patient/patientdetails.html', context)
#


def get_customer_details(request, email: str):
    customer = hotel_service_provider.customer_management_service().get_customer_by_email(email=email)
    context = {
        'customer': customer
    }
    return render(request, 'customer/view_details.html', context)


def __create_customer_if_post_method(request, context):
    if request.method == 'POST':
        try:

            customer = __get_attribute_from_request(request)
            if customer.password == customer.confirm_password:
                hotel_service_provider.customer_management_service().create_customer(customer)
                context['saved'] = True
            else:
                context['saved'] = False
        except Exception as e:
            raise e


def list_customer_if_post_method(request):
    customers = hotel_service_provider.customer_management_service().list_customers()
    context = {
        'customers': customers
    }
    return render(request, 'customer/list_customers.html', context)


def list_customer_by_a_particular_term(request):
    term = __get_attribute_for_listing_if_post_method(request)[0]
    customers = hotel_service_provider.customer_management_service().list_customers_by_a_particular_term(term)
    context = {
        'customers': customers
    }
    return render(request, 'customer/list_customers_by_a_particular_term.html', context)


def __get_attribute_for_listing_if_post_method(request: HttpRequest):
    term = request.POST['term']
    return term
