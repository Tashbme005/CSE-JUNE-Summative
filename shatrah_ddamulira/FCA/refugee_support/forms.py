from django import forms
from django.forms import ModelForm
from .models import Refugee


class RefugeeForm(ModelForm):
    class Meta:
        model = Refugee
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'date_of_birth': 'Date of Birth',
            'place_of_birth': 'Place of Birth',
            'gender': 'Gender',
            'nationality': 'Nationality',
            'marital_status': 'Marital Status',
            'settlement_camp': 'Settlement Camp',
            'date_of_joining_settlement_camp': 'Date of Joining Settlement Camp',
        }

        error_messages = {
            'first_name': {
                'required': 'This field is required.',
                'invalid': 'Invalid field.'
            },
            'last_name': {
                'required': 'This field is required.',
                'invalid': 'Invalid field.'
            },
            'date_of_birth': {
                'required': 'This field is required.',
                'invalid': 'Invalid field.'
            },
            'place_of_birth': {
                'required': 'This field is required.',
                'invalid': 'Invalid field.'
            },
            'settlement_camp': {
                'required': 'This field is required.',
                'invalid': 'Invalid field.'
            },
            'date_of_joining_settlement_camp': {
                'required': 'This field is required.',
                'invalid': 'Invalid field.'
            },
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'place_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'nationality': forms.Select(attrs={'class': 'form-select'}),
            'marital_status': forms.Select(attrs={'class': 'form-select'}),
            'settlement_camp': forms.Select(attrs={'class': 'form-select'}),
            'date_of_joining_settlement_camp': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

        