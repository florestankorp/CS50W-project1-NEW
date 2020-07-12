from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("edit/<str:name>/", views.edit, name="edit"),
    path("random", views.random, name="random"),
    path("search", views.search, name="search"),
    path("<str:entry>", views.entry, name="entry"),
]
