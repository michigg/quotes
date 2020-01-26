"""fachschaftszitat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from fachschaftszitat import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('videos/', views.registration_gif, name='gifs'),
    path('quote-registration/', views.registration_quote, name="register_quote"),
    path('author-registration/', views.registration_author, name="register_author"),
    path('api/', include('fachschaftszitat.api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
