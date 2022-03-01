from django import forms
# from betterforms.multiform import MultiModelForm
from events.models import (
    EventCategory,
    Event,
    EventImage,
    EventAgenda,
)


class EventForm(forms.Form):
    """
    The Event form.
    """
    class Meta:
        model = Event
        fields = ['category', 'name', 'uid', 'description', 'job_category', 'scheduled_status', 'venue', 'start_date', 'end_date', 'location', 'price', 'points', 'maximum_attendee', 'status']
        widgets = {
            'start_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class EventImageForm(forms.ModelForm):


    class Meta:
        model = EventImage
        fields = ['image']



class EventAgendaForm(forms.ModelForm):


    class Meta:
        model = EventAgenda
        
        fields = ['session_name', 'speaker_name', 'start_time', 'end_time', 'venue_name']

        widgets = {
            'start_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
        }


# class EventCreateMultiForm(MultiModelForm):
#     form_classes = {
#         'event': EventForm,
#         'event_image': EventImageForm,
#         'event_agenda': EventAgendaForm,
#     }


class EventAgendaForm(forms.Form):
    class Meta:
        model = EventAgenda
        fields = "_all_"
        widgets = {

        }


class SmsFormView(forms.Form):

    def sendSMS(self, phone_number, message):
        import requests
        import json
        import urllib.parse

        url = "https://www.fast2sms.com/dev/bulk"
        payload = "sender_id=FSTSMS&message=" + message + "&language=english&route=p&numbers=" + phone_number
        headers = {
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        # print(res/ponse.text)

        number = "256" + phone_number

        random_code = [i for i in range(10)]
        random_code = "".join(str(i) for i in random_code)

        return response.text
