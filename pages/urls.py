# pages/urls.py
from django.urls import path
from .views import HomePageView
from .views import SignUpView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
