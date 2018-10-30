from django import forms
from fachschaftszitat.models import Statement, Quote, Author
from django.forms import modelformset_factory
import datetime


class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['author', 'text']


class QuoteForm(forms.ModelForm):
    timestamp = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = Quote
        fields = ['timestamp']


StatementFormset = modelformset_factory(
    Statement,
    fields=('author', 'text'),
    extra=1
)


class AuthorsForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
