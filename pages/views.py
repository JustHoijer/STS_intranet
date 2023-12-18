# pages/views.py
from django.views.generic import TemplateView

from django.shortcuts import render


class LandingPageView(TemplateView):
    template_name = "pages/landing.html"

    def under_dev(request, page_name):
        return render(request, "pages/under_dev.html", {"page_name": page_name})
