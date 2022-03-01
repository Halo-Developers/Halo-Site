from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

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


class EventCategory(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a event category instance.
    """
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    # permission_classes = (IsAuthenticated,)


class EventCategoryList(generics.ListCreateAPIView):
    """
    List all event categories, or create a new event category.
    """
    # queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    # permission_classes = (IsAuthenticated,)


class JobCategory(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a job category instance.
    """
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer
    

class JobCategoryList(generics.ListCreateAPIView):
    """
    List all job categories, or create a new job category.
    """
    # queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer


class EventMember(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a event member instance.
    """
    queryset = EventMember.objects.all()
    serializer_class = EventMemberSerializer

class EventMemberList(generics.ListCreateAPIView):
    """
    List all event members, or create a new event member.
    """

    # queryset = EventMember.objects.all()
    serializer_class = EventMemberSerializer

class EventUserWhishList(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a event user whish list instance.
    """
    # queryset = EventUserWhishList.objects.all()
    serializer_class = EventUserWhishList


class UserCoin(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user coin instance.
    """
    queryset = UserCoin.objects.all()
    serializer_class = UserCoinSerializer

class UserCoinList(generics.ListCreateAPIView):
    """
    List all user coins, or create a new user coin.
    """
    # queryset = UserCoin.objects.all()
    serializer_class = UserCoinSerializer


class EventAgenda(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a event agenda instance.
    """
    queryset = EventAgenda.objects.all()
    serializer_class = EventAgendaSerializer


class EventAgendaList(generics.ListCreateAPIView):
    """
    List all event agendas, or create a new event agenda.
    """
    # queryset = EventAgenda.objects.all()
    serializer_class = EventAgendaSerializer


class EventImage(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a event image instance.
    """
    queryset = EventImage.objects.all()
    serializer_class = EventImageSerializer


class EventJobCategoryLinking(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a event job category linking instance.
    """
    queryset = EventJobCategoryLinking.objects.all()
    serializer_class = EventJobCategoryLinkingSerializer
    
