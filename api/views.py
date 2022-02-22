from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from .serializers import (
    EventSerializer,
    EventCategorySerializer
)

from events.models import (
    EventCategory,
    Event,
)


class EventView(viewsets.ModelViewSet):
    """
    The Event view.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
