from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from .serializers import (
    EventSerializer,
    EventCategorySerializer,
    JobCategorySerializer,
    EventMemberSerializer,
    EventUserWhishList,
    UserCoinSerializer,
    EventAgendaSerializer,
    EventImageSerializer,
    EventJobCategoryLinkingSerializer
)

from events.models import (
    Event,
    EventCategory,
    JobCategory,
    EventAgenda,
    EventJobCategoryLinking,
    EventMember,
    EventUserWishList,
    UserCoin,
    EventImage,
)


class EventView(viewsets.ModelViewSet):
    """
    The Event view.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
