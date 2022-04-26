from django.forms import ModelForm, widgets
from .models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from crispy_forms.bootstrap import InlineCheckboxes, FormActions
from django.utils.translation import ugettext_lazy as _
import datetime as dt
from django.urls import reverse


class Dentist_Form(ModelForm):
    class Meta:
        model = Dentist
        fields = '__all__'
        labels = {
            'last_name': _('Last Name*'),
            'first_name': _('First Name*'),
            'middle_name': _('Middle Name'),
            'email_address': _('Email Address*'),
            'contact_number': _('Contact Number*'),
            'years_of_service': _('Years Of Service*'),
        }
        widgets = {
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Enter Middle Name'}),
            'email_address': forms.EmailInput(attrs={'placeholder': 'Enter Email Address'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Enter Contact Number'}),
            'years_of_service': forms.NumberInput(attrs={'placeholder': 'Enter Years Of Service'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('last_name'),
                Column('first_name'),
                Column('middle_name'),
            ),
            Row(
                Column('email_address'),
                Column('contact_number'),
                Column('years_of_service'),
            ),
            FormActions(
                Submit('Save', 'Save', css_class="btn btn-success"),
            ),
        )
     


class Patient_Form(ModelForm):
    class Meta:
        model = Patient
        fields = ('last_name','first_name','middle_name','street','city','province','zip_code', 'contact_number','email_address')

        labels = {
            'last_name': _('Last Name*'),
            'first_name': _('First Name*'),
            'middle_name': _('Middle Name'),
            'email_address': _('Email Address*'),
            'contact_number': _('Contact Number*'),
            'years_of_service': _('Years Of Service*'),
            'street': _('Street*'),
            'city': _('City*'),
            'province': _('Province'),
            'zip_code': _('Zip Code*'),
        }
        widgets = {
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Enter Middle Name'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Enter Contact Number'}),
            'street': forms.TextInput(attrs={'placeholder': 'Enter Street'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter City'}),
            'province': forms.TextInput(attrs={'placeholder': 'Enter Province'}),
            'zip_code': forms.NumberInput(attrs={'placeholder': 'Enter Zip Code'}),
            'email_address': forms.EmailInput(attrs={'placeholder': 'Enter Email Address'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('last_name'),
                Column('first_name'),
                Column('middle_name'),
            ),
            Row(
                Column('email_address'),
                Column('contact_number'),
            ),
            Row(
                Column('street'),
                Column('city'),
                Column('province'),
                Column('zip_code'),
            ),
            FormActions(
                Submit('Save', 'Save', css_class="btn btn-success"),
            ),
        )

class Book_Patient_Form(ModelForm):
    class Meta:
        model = Patient
        fields = ('last_name','first_name','middle_name','street','city','province','zip_code', 'contact_number','email_address')

        labels = {
            'last_name': _('Last Name*'),
            'first_name': _('First Name*'),
            'middle_name': _('Middle Name'),
            'email_address': _('Email Address*'),
            'contact_number': _('Contact Number*'),
            'years_of_service': _('Years Of Service*'),
            'street': _('Street*'),
            'city': _('City*'),
            'province': _('Province'),
            'zip_code': _('Zip Code*'),
        }

class Procedure_Form(ModelForm):
    class Meta:
        model = Procedure
        fields = '__all__'
        labels = {
            'title': _('Procedure Title*'),
            'price': _('Price*'),
            'description': _('Description*'),
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter Procedure Title'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter Price'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter Description'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title'),
                Column('price'),
            ),
            'description',
            FormActions(
                Submit('Save', 'Save', css_class="btn btn-success"),
            ),
        )

class DateInput(forms.DateInput):
    input_type = 'date'

class Appointment_Form(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        labels = {
            'date_of_appointment': _('Appointment Date*'),
            'time_of_appointment': _('Appointment Time*'),
            'patient': _('Patient*'),
            'dentist': _('Dentist*'),
            'procedures': _('Procedures*'),
        }
        widgets = {
            'date_of_appointment': DateInput(),
            'time_of_appointment': forms.Select,
            'patient': forms.Select,
            'dentist': forms.Select,
            'procedures': forms.CheckboxSelectMultiple,
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('date_of_appointment'),
                Column('time_of_appointment'),
            ),
            Row(
                Column('patient'),
                Column('dentist'),
            ),
            InlineCheckboxes('procedures'),
            FormActions(
                Submit('Save', 'Save', css_class="btn btn-success"),
            ),
        )

class Book_Appointment_Form(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        labels = {
            'date_of_appointment': _('Appointment Date*'),
            'time_of_appointment': _('Appointment Time*'),
            'dentist': _('Dentist*'),
            'procedures': _('Procedures*'),
        }
        widgets = {
            'date_of_appointment': DateInput(),
            'time_of_appointment': forms.Select,
            'patient': forms.HiddenInput(),
            'dentist': forms.Select,
            'procedures': forms.CheckboxSelectMultiple,
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('date_of_appointment'),
                Column('time_of_appointment'),
            ),
            Row(
                Column('dentist'),
                Column('patient'),
            ),
            InlineCheckboxes('procedures'),
            FormActions(
                Submit('Save', 'Save', css_class="btn btn-success"),
            ),
        )
        


class Record_Form(ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
        labels = {
            'appointment': _('Appointment*'),
            'status': _('Status*'),
        }

        widgets = {
                'appointment': forms.Select,
                'status': forms.Select,
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('appointment'),
                Column('status'),
            ),
            FormActions(
                Submit('Save', 'Save', css_class="btn btn-success"),
            ),
        )