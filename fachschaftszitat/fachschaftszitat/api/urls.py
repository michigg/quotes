from django.urls import path
from fachschaftszitat.api import views
app_name = 'fachschaftszitat.api'
urlpatterns = [
    path('quote/latest/', views.ApiGetLatestQuote.as_view(), name='test'),
]