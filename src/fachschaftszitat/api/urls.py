from django.urls import path
from fachschaftszitat.api import views

app_name = 'fachschaftszitat.api'
urlpatterns = [
    path('quote/latest/', views.ApiGetLatestQuote.as_view(), name='last-quote'),
    path('quote/', views.ApiGetQuotes.as_view(), name='quotes'),
    path('quote/<int:pk>/', views.ApiRemoveQuote.as_view(), name='delete-quote'),
    path('author/', views.ApiGetAuthors.as_view(), name='authors'),
    path('gifs/', views.ApiGifs.as_view(), name='gifs'),
]
