from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Note
from .forms import NoteForm


class NoteListView(LoginRequiredMixin, ListView):
    model = Note

    def get_queryset(self):
        return self.request.user.note_set.all()


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('notes:list')
