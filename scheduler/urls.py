from django.urls import re_path, path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "scheduler"
urlpatterns = [
    # URL pattern for the main index view
    re_path(r"^$", views.index, name="index"),
    # URL pattern for updating an event with a specific ID
    re_path(r"^data/(?P<pk>[0-9]+)$", views.event_update),
    # URL pattern for listing or adding data (events or other) based on the provided parameter
    re_path(r"^data/(.*)$", views.data_list),
    # URL pattern for checking dates
    path("check/", views.data_check, name="check_dates"),
]

# Apply REST framework's format_suffix_patterns to the URL patterns
urlpatterns = format_suffix_patterns(urlpatterns)
