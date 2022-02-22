import imp
from django.urls import path, include

from .views import (
    # EventView,
    EventCategoryListView,
)
from rest_framework import routers
from api.api import (
    EventList,
    EventDetail,
)


router = routers.DefaultRouter()
# router.register(r'events', EventView, 'event')


"""Routing the views from the events app"""
urlpatterns = [
    path('category-list/', EventCategoryListView.as_view(), name='event-category-list'),
    # path('api/', include(router.urls)),
]


""""This is the api urls endpoint"""
urlpatterns += [
    path('api/events/', EventList.as_view(), name='event-list'),
    path('api/events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
]