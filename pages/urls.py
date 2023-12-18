# pages/urls.py

from django.urls import path

from .views import LandingPageView

# Define an app name to create a namespace for the app's URLs
app_name = "pages"

urlpatterns = [
    path("", LandingPageView.as_view(), name="landing"),
    path("dev/<str:page_name>/", LandingPageView.under_dev, name="under_dev"),
]
