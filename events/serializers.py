"""This file contains the serializer for the events."""
from rest_framework import serializers
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

class EventSerializer(serializers.ModelSerializer):
    """
    The Event serializer.
    """
    class Meta:
        """
        The meta class.
        """
        model = Event
        fields = ('id', 'category', 'name', 'uid', 'description', 'job_category', 'scheduled_status', 'venue', 'start_date', 'end_date', 'location', 'price', 'points', 'maximum_attendee', 'status', 'created_user', 'updated_user', 'created_at', 'updated_at')


class EventCategorySerializer(serializers.ModelSerializer):
    """
    The EventCategory serializer.
    """
    class Meta:
        """
        The meta class.
        """
        model = EventCategory
        fields = ('id', 'name', 'code', 'priority', 'created_user', 'updated_user', 'created_date', 'updated_date', 'status')


