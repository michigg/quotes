from django.shortcuts import render
from fachschaftszitat.models import Quote
from fachschaftszitat.forms import QuoteForm, AuthorsForm
from django.http.response import HttpResponse, HttpResponseRedirect


# Create your views here.
def home(request):
    quotes = Quote.objects.all()
    quote_form = QuoteForm()
    author_form = AuthorsForm()
    return render(request, 'home.jinja', {'quotes': quotes, 'quoteform': quote_form, 'authorform': author_form})


def registration_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.jinja', {})
    return render(request, 'error.jinja', {})


def registration_author(request):
    if request.method == 'POST':
        form = AuthorsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.jinja', {})
        return render(request, 'error.jinja', {})
