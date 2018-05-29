from django.db import models
from django import forms
import re


class Note(models.Model):
    count_unique_words = models.IntegerField()
    title = models.CharField(max_length=70)
    publication_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.text

    @classmethod
    def create(cls, title, text):
        note = cls(title=title, text=text)
        # calculation unique words count
        words = re.split(r'\.|,|:| |!|\?', str(text).lower())
        note.count_unique_words = len(set(words))
        return note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']
