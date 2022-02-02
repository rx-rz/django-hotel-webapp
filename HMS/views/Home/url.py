from django.urls import path
from HMS.views.Home import view

urlpatterns = [
    path('home', view.home, name='home'),
    path('rooms', view.rooms, name='rooms'),
    path('contacts', view.contacts, name='contacts'),
    path('social', view.social, name='social'),
    path('tranquille_desprit', view.tranquille_desprit, name='tranquille')
]
