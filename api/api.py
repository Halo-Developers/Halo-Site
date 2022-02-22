from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from events.models import (
    EventCategory,
    Event,
    EventAgenda,
    EventJobCategoryLinking,
    EventMember,
    EventUserWishList,
    UserCoin,
    EventImage,
)

from .serializers import (
    EventSerializer,
    EventCategorySerializer,
    JobCategorySerializer,
    EventAgendaSerializer,
    EventJobCategoryLinkingSerializer,
    EventMemberSerializer,
    # EventUserWishListSerializer
    UserCoinSerializer,
    EventImageSerializer,
)


class EventList(generics.ListCreateAPIView):
    """
    List all events, or create a new event.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = (IsAuthenticated,)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a event instance.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = (IsAuthenticated,)
