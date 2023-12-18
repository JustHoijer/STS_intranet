from django.urls import path

from .views import (
    index_display,
    display,
    edit_display,
    delete_display,
    create_display,
    slide_create,
    slide_detail,
    slide_edit,
    slide_delete,
)

# Define an app name to create a namespace for the app's URLs
app_name = "display_board"

# Define the URL patterns for the "landing" app
urlpatterns = [
    # Default URL pattern for the home page
    path("", index_display, name="index"),
    path("<int:pk>/", display, name="display"),
    path("edit_display/<int:pk>/", edit_display, name="edit_display"),
    path("delete_display/<int:pk>/", delete_display, name="delete_display"),
    path("create_display/", create_display, name="create_display"),
    path("slide_create/<int:pk>/", slide_create, name="slide_create"),
    path("slide_detail/<int:pk>/", slide_detail, name="slide_detail"),
    path("slide_edit/<int:pk>/", slide_edit, name="slide_edit"),
    path("slide_delete/<int:pk>/", slide_delete, name="slide_delete"),
]
