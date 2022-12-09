from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["title", "text"]

    def clean_title(self):
        title = self.cleaned_data["title"]

        if "Django" not in title:
            raise ValidationError("Only accepting notes about Django")

        return title
