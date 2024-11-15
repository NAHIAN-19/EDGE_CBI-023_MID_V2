from django.urls import path
from events import views
urlpatterns = [
    path('events/upcomming/',views.EventView.as_view()),
]
