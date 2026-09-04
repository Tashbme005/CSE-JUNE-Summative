from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landing_page'),
    path('registration_form.html/', views.registration_form, name='registration_form'),
]