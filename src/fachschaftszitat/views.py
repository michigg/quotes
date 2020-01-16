import os
import random
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

from core.settings import STATICFILES_DIRS, STATIC_URL
from fachschaftszitat.forms import QuoteForm, AuthorsForm, StatementFormset
from fachschaftszitat.models import Quote, Author, Statement

import logging

logger = logging.getLogger(__name__)


def get_random_sucess_url():
    file = random.choice(os.listdir(os.path.join(STATICFILES_DIRS[0], 'images/success')))
    return STATIC_URL + 'images/success/' + file


def get_random_error_url():
    file = random.choice(os.listdir(os.path.join(STATICFILES_DIRS[0], 'images/oops')))
    return STATIC_URL + 'images/oops/' + file


# Create your views here.
@login_required
def home(request):
    if request.user.is_authenticated:
        print(request.user.groups.all())
        groups = request.user.groups.all()
        quote_form = QuoteForm(None)
        statement_formset = StatementFormset(queryset=Statement.objects.none())
        author_form = AuthorsForm()
        authors = Author.objects.all().order_by('name')
        today_date = datetime.today()
        return render(request, 'home.jinja2',
                      {'quote_form': quote_form, 'statement_formset': statement_formset,
                       'authorform': author_form, 'authors': authors, 'user_groups': groups,
                       'today_date': today_date})
    return render(request, 'home.jinja2')


@login_required
def registration_quote(request):
    logger.error("call")
    if request.user.is_authenticated and request.method == 'POST':
        quote_form = QuoteForm(request.POST)
        statement_form = StatementFormset(request.POST)
        if statement_form.is_valid() and quote_form.is_valid():
            pre_saves = statement_form.save(commit=False)
            order_id = 1
            for pre_save in pre_saves:
                pre_save.order_id = order_id
                order_id += 1
                pre_save.save()
    #         logger.info("statements_savedee")
            quote = quote_form.save(commit=False)
            quote.creator = request.user
            quote.save()
            quote.statements.add(*pre_saves)
            quote.save()
            return JsonResponse({'url': get_random_sucess_url()}, status=201)
    return JsonResponse({'url': get_random_error_url()}, status=400)


@login_required
def registration_author(request):
    if request.method == 'POST':
        form = AuthorsForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'url': get_random_sucess_url()}, status=201)
        return JsonResponse({'url': get_random_error_url()}, status=400)
