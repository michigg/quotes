from django.urls import path
from fachschaftszitat.api import views
app_name = 'fachschaftszitat.api'
urlpatterns = [
    path('quote/latest/', views.ApiGetLatestQuote.as_view(), name='last-quote'),
    path('quote/', views.ApiGetQuotes.as_view(), name='quotes'),
]