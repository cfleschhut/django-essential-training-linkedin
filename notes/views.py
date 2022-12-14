from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Note
from .forms import NoteForm


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    login_url = "/admin/"

    def get_queryset(self):
        return self.request.user.note_set.all()


class NoteDetailView(DetailView):
    model = Note


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    success_url = "/notes/"


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    success_url = "/notes/"


class NoteDeleteView(DeleteView):
    model = Note
    success_url = "/notes/"
