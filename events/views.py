from django.shortcuts import render
from django.views.generic import (
    ListView,
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import (
    EventCategory,
)

""""Event category List View"""
class EventCategoryListView(LoginRequiredMixin, ListView):
    # login_url = 'login'
    model = EventCategory
    template_name = "events/event_category.html"
    context_object_name = "event_category"