from django.urls import path
from core.views import home, contact

# example.com
urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact')
]