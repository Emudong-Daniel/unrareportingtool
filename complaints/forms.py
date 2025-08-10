# complaints/forms.py
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Complaint, StatusUpdate

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'contact', 'email', 'location', 'description', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your contact'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Location'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe the issue in detail'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = StatusUpdate
        fields = ['status', 'comment']
        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Optional comment on status change'
            }),
        }

class LookupForm(forms.Form):
    complaint_id = forms.IntegerField(
        label='Complaint ID',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., 123'
        })
    )
    contact = forms.CharField(
        label='Contact',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'The contact used on submission'
        })
    )

class ReportForm(forms.Form):
    start_date = forms.DateField(
        required=False,
        label='From',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )
    end_date = forms.DateField(
        required=False,
        label='To',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )
    status = forms.ChoiceField(
        required=False,
        label='Status',
        choices=[('', 'All')] + Complaint.STATUS_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    location = forms.CharField(
        required=False,
        label='Location contains…',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Filter by location keyword'
        })
    )
