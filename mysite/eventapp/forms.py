from django import forms
from .models import CreateEvent

class EventForm(forms.ModelForm):
    class Meta:
        model = CreateEvent
        fields = ['title', 'date', 'location', 'description']
        