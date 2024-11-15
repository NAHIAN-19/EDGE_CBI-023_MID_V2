from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'date', 'location']
    
admin.site.register(Event,EventAdmin)
