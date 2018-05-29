from django.shortcuts import render
from notes.models import Note, NoteForm
import django.http


def index(request):
    # sorting in reverse order
    notes = Note.objects.all().order_by('-count_unique_words')
    return render(request, 'notes/index.html', {'notes': notes})


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            Note.create(title=title, text=text).save()
            return django.http.HttpResponseRedirect("/notes/")
        else:
            return render(request, 'notes/form_is_not_valid.html')
    else:
        form = NoteForm()
        return render(request, 'notes/add_note.html', {'form': form})
