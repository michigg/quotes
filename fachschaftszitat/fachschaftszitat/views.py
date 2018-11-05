import os
import random
from datetime import datetime

from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

from core.settings import STATICFILES_DIRS, STATIC_URL
from fachschaftszitat.forms import QuoteForm, AuthorsForm, StatementFormset
from fachschaftszitat.models import Quote, Author, Statement


def get_random_sucess_url():
    file = random.choice(os.listdir(os.path.join(STATICFILES_DIRS[0], 'images/success')))
    return STATIC_URL + 'images/success/' + file


def get_random_error_url():
    file = random.choice(os.listdir(os.path.join(STATICFILES_DIRS[0], 'images/oops')))
    return STATIC_URL + 'images/oops/' + file


# Create your views here.
def home(request):
    quotes = Quote.objects.all().order_by('-timestamp')
    quote_form = QuoteForm(None)
    statement_formset = StatementFormset(queryset=Statement.objects.none())
    author_form = AuthorsForm()
    authors = Author.objects.all().order_by('name')
    today_date = datetime.today()
    todays_author = Author.objects.annotate(num_statements=Count('statement')).order_by('num_statements')
    print(todays_author)
    return render(request, 'home.jinja',
                  {'quotes': quotes, 'quote_form': quote_form, 'statement_formset': statement_formset,
                   'authorform': author_form, 'authors': authors,
                   'today_date': today_date, 'todays_author': todays_author})


def registration_quote(request):
    if request.method == 'POST':
        quote_form = QuoteForm(request.POST)
        statement_form = StatementFormset(request.POST)
        if statement_form.is_valid() and quote_form.is_valid():
            pre_saves = statement_form.save(commit=False)
            order_id = 1
            for pre_save in pre_saves:
                pre_save.order_id = order_id
                order_id += 1
                pre_save.save()
            quote = quote_form.save()
            quote.statements.add(*pre_saves)
            quote.save()
            return JsonResponse({'url': get_random_sucess_url()}, status=201)
    return JsonResponse({'url': get_random_error_url()}, status=400)


def registration_author(request):
    if request.method == 'POST':
        form = AuthorsForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'url': get_random_sucess_url()}, status=201)
        return JsonResponse({'url': get_random_error_url()}, status=400)
