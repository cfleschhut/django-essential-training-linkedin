from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('notes:detail', kwargs={'pk': self.pk})
