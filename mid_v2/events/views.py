from django.shortcuts import render
from events.models import Event

from django.views.generic import ListView
from datetime import date
class EventView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'
    
    def get_queryset(self):
        return Event.objects.filter(date__gte=date.today())
    