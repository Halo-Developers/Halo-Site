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


class JobCategorySerializer(serializers.ModelSerializer):
    """
    The JobCategory serializer.
    """
    class Meta:
        """
        The meta class.
        """
        model = JobCategory
        fields = ('id', 'name')


class EventMemberSerializer(serializers.ModelSerializer):
    """
    The EventMember serializer.
    """
    class Meta:
        """
        The meta class.
        """
        model = EventMember
        fields = ('id', 'event', 'user', 'attend_status', 'status', 'created_user', 'updated_user', 'created_date', 'updated_date')


class EventUserWhishList(serializers.ModelSerializer):
    """
    The Event User Whish List serializer.
    """
    class Meta:
        """
        The meta class.
        """
        model = EventUserWishList
        fields = ('id', 'event', 'user', 'status', 'created_user', 'updated_user', 'created_date', 'updated_date')


class UserCoinSerializer(serializers.ModelSerializer):
    """
    The UserCoin serializer.
    """
    class Meta:
        """
        The meta class.
        """
        model = UserCoin
        fields = ('id', 'user', 'gain_type', 'gain_coin', 'status', 'created_user', 'updated_user', 'created_date', 'updated_date')


class EventAgendaSerializer(serializers.ModelSerializer):
    """
    The EventAgenda serializer.
    """
    class Meta:
        """
        The meta class.
        """
        model = EventAgenda
        fields = ('id', 'event', 'session_name', 'speaker_name', 'start_date', 'end_date', 'venue_name')


class EventImageSerializer(serializers.ModelSerializer):
    """
    The EventImage serializer.
    """
    class Meta:
        """
        The meta class.
        """
        model = EventImage
        fields = ('id', 'event', 'image')


class EventJobCategoryLinkingSerializer(serializers.ModelSerializer):
    """
    The Event Job Category Linking serializer.
    """
    class Meta:
        """
        The meta class.
        """
        model = EventJobCategoryLinking
        fields = ('id', 'event', 'job_category', 'status')