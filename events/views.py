from django.shortcuts import render
from rest_framework import viewsets

from django.views.generic import (
    ListView,
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import (
    EventCategory,
    Event,
)


from .forms import EventForm, EventImageForm, EventAgendaForm #EventCreateMultiForm


""""Event category List View"""
class EventCategoryListView(LoginRequiredMixin, ListView):
    # login_url = 'login'
    model = EventCategory
    template_name = "events/event_category.html"
    context_object_name = "event_category"



class EventCategoryListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = EventCategory
    template_name = 'events/event_category.html'
    context_object_name = 'event_category'


# class EventCategoryCreateView(LoginRequiredMixin, CreateView):
#     login_url = 'login'
#     model = EventCategory
#     fields = ['name', 'code', 'image', 'priority', 'status']
#     template_name = 'events/create_event_category.html'

#     def form_valid(self, form):
#         form.instance.created_user = self.request.user
#         form.instance.updated_user = self.request.user
#         return super().form_valid(form)
