import os
import random
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

from core.settings import STATICFILES_DIRS, STATIC_URL
from fachschaftszitat.forms import QuoteForm, AuthorsForm, StatementFormset, GifForm
from fachschaftszitat.models import Quote, Author, Statement, Gif

import logging

logger = logging.getLogger(__name__)


def get_random_sucess_url():
    gifs = Gif.objects.filter(type=Gif.SUCCESS)
    gif_urls = [gif.video_url for gif in gifs]
    files = os.listdir(os.path.join(STATICFILES_DIRS[0], 'images/success'))
    file_based_gif_urls = [f'{STATIC_URL}images/success/{file}' for file in files]
    gif_urls.extend(file_based_gif_urls)
    return random.choice(gif_urls)


def get_random_error_url():
    gifs = Gif.objects.filter(type=Gif.ERROR)
    gif_urls = [gif.video_url for gif in gifs]
    files = os.listdir(os.path.join(STATICFILES_DIRS[0], 'images/oops'))
    file_based_gif_urls = [f'{STATIC_URL}images/oops/{file}' for file in files]
    gif_urls.extend(file_based_gif_urls)
    return random.choice(gif_urls)


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


@login_required
def registration_gif(request):
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            gif = form.save(commit=False)
            if is_video_url_valid(gif.video_url):
                gif.creator = request.user
                gif.save()
                return JsonResponse({'url': get_random_sucess_url()}, status=201)
        return JsonResponse({'url': get_random_error_url()}, status=400)
    else:
        gifs = Gif.objects.filter(creator=request.user)
        form = GifForm()
    return render(request, 'gif.jinja2', {"form": form, "gifs": gifs})


def is_video_url_valid(url):
    url_starts = ["https://media.giphy.com/media/", "https://media.tenor.com/videos/"]
    url_ends = [".mp4", "/mp4"]
    has_known_url_start = any([url.startswith(url_start) for url_start in url_starts])
    has_known_url_end = any([url.endswith(url_end) for url_end in url_ends])

    return has_known_url_start and has_known_url_end
