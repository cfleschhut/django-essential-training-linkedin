from django.urls import path

from . import views

app_name = "notes"

urlpatterns = [
    path("notes/", views.NoteListView.as_view(), name="list"),
    path("notes/<int:pk>/", views.NoteDetailView.as_view(), name="detail"),
    path("notes/new/", views.NoteCreateView.as_view(), name="new"),
    path("notes/<int:pk>/edit/", views.NoteUpdateView.as_view(), name="update"),
    path("notes/<int:pk>/delete/", views.NoteDeleteView.as_view(), name="delete")
]
