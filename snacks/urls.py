from django.urls import path
from .views import HomePageView, AboutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
]