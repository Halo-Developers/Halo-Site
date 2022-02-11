"""This file contains the serializer for the events."""
from rest_framework import serializers
from events.models import Event

class EventSerializer(serializers.ModelSerializer):
    """
    The Event serializer.
    """
    class Meta:
        """
        The meta class.
        """
        model = Event
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'location', 'price', 'image', 'created_at', 'updated_at')



"""Chapter Mentor : Mr. Tonny Engwau
Chapter President : Kuyeso Rogers
Vice President : Kataike Gloria 
Secretary : Ahimbisimbwe Sam
Vice sec: Shakira Hadijah 
Event Community Mobilizer : Mbabali Faisal
Student Government Representative : Sebayiga Abraham
Finance : """

