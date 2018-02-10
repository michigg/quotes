from django.shortcuts import render
from fachschaftszitat.models import Quote, Author
from fachschaftszitat.forms import QuoteForm, AuthorsForm
from datetime import datetime


# Create your views here.
def home(request):
    quotes = Quote.objects.all().order_by('-timestamp')
    quote_form = QuoteForm()
    author_form = AuthorsForm()
    authors = Author.objects.all().order_by('name')
    today_date = datetime.today()
    return render(request, 'home.jinja',
                  {'quotes': quotes, 'quoteform': quote_form, 'authorform': author_form, 'authors': authors,
                   'today_date': today_date})


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
