from django.db import models
from django import forms
import re
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler('log.txt'))


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
        words =  set(re.split(r'[.,: !?\n\r\t-]+', str(text).lower()))
        if '' in words:
                words.remove('')
        logger.debug('Adding note "%s". Unique words: %s'%(str(note), str(words)))
        note.count_unique_words = len(words)
        return note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']
