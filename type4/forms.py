from django import forms
from django.forms.extras.widgets import SelectDateWidget

class ChangesForm(forms.Form):
	YEAR_CHOICES = ['2014','2015']
	from_timestamp = forms.DateTimeField(
		widget=SelectDateWidget(years=YEAR_CHOICES))
	to_timestamp = forms.DateTimeField(
		widget=SelectDateWidget(years=YEAR_CHOICES))