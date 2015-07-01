from django import forms
from models import Booking, Enquiry


class  BookingForm(forms.ModelForm):
	class Meta:
		model = Booking
		exclude = ['created_at']

class  EnquiryForm(forms.ModelForm):
	class Meta:
		model = Enquiry
		exclude = ['created_at']