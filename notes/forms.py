from django.forms import ModelForm, TextInput, Textarea
from django.core.exceptions import ValidationError

from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["title", "text"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "text": Textarea(attrs={"class": "form-control"})
        }
        labels = {
            "text": "Write your thoughts here:"
        }

    def clean_title(self):
        title = self.cleaned_data["title"]

        if "Django" not in title:
            raise ValidationError("Only accepting notes about Django")

        return title
