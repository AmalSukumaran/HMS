from django import forms

from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["p_name", "p_phone", "p_email","p_user","doc_name", "booking_date"]

        widgets = {
            'booking_date': DateInput
        } 

        labels = {
            'p_name': "Patient Name: ",
            'p_phone': "Patient Phone: ",
            'p_email': "Patient Email: ",
            'doc_name': "Doctor Name: ",
            'booking_date': "Booking date: ",
        }