from django.urls import path
from HMS.views.login import view


urlpatterns = [
    path('auth', view.login_get, name='login_get'),
    path('login', view.login_post, name='login_post'),
    path('logout', view.log_out, name='log_out'),
    path('profile', view.profile, name='profile'),
]
