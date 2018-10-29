from django import forms
from fachschaftszitat.models import Quote, Author
import datetime


class QuoteForm(forms.ModelForm):
    timestamp = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = Quote
        fields = ['timestamp', 'statements']


class AuthorsForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
