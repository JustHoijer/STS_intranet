# pages/views.py
from django.views.generic import TemplateView

# from django.shortcuts import render


class LandingPageView(TemplateView):
    template_name = "landing.html"
