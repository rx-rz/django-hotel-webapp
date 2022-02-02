from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from HMS.service_provider import *
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize


def login_get(request):
    context = {
        'next': request.GET.get('next', 'home')
    }
    return render(request, 'authorization/login.html', context)


def login_post(request):
    context = dict()
    resolve_url = request.GET.get('next')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user: User = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        groups = serialize('json', request.user.groups.all())
        request.session['groups'] = groups
        return redirect(resolve_url)
    else:
        context['message'] = 'username or password incorrect'
        return render(request, 'authorization/login.html', context)


def log_out(request):
    logout(request)
    return redirect("home")


@login_required(redirect_field_name='next')
def profile(request):
    groups = request.session.get('groups')
    if 'Customers' in groups:
        user_id = request.user.id
        customer = hotel_service_provider.customer_management_service().customer_details(user_id)
        context = {
            'customer_first_name': customer.first_name,
            'customer_last_name': customer.last_name,
        }
        return render(request, 'customer/dashboard.html', context)
    elif 'Managers' in groups:
        user_id = request.user.id
        manager = hotel_service_provider.manager_management_service().manager_details(user_id)
        context = {
            'first_name': manager.first_name
        }
        return render(request, 'manager/dashboard.html', context)

