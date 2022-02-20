import imp
from django.urls import path

from .views import (
    EventCategoryListView,
)

urlpatterns = [
    path('category-list/', EventCategoryListView.as_view(), name='event-category-list')
]