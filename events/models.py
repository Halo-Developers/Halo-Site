from django.db import models
from django.urls import reverse

"""Imported models"""
from mapbox_location_field.models import LocationField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


"""Event Category Models are literally defined here"""
class EventCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=6, unique=True)
    image = models.ImageField(upload_to='media/')
    priority = models.IntegerField(unique=True)
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status_choice = (
        ('disabled', 'Disabled'),
        ('active', 'Active'),
        ('deleted', 'Deleted'),
        ('blocked', 'Blocked'),
        ('completed', 'Completed'),
    )
    status = models.CharField(choices=status_choice, max_length=10)

    def __str__(self):
        return f"Event Category is {self.name}"

    def get_absolute_url(self):
        return reverse("event-category-list", kwargs={"pk": self.pk})


    
""""The models containing the data for the events app."""
class Event(models.Model):
    """
    The Event model.
    """
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    uid = models.PositiveIntegerField(unique=True)
    description = RichTextUploadingField()
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    select_scheduled_status = (
        ('yet to scheduled', 'Yet to Scheduled'),
        ('scheduled', 'Scheduled')
    )
    scheduled_status = models.CharField(max_length=25, choices=select_scheduled_status)
    venue = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    location = LocationField()
    points = models.PositiveIntegerField()
    maximum_attende = models.PositiveIntegerField()
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True, related_name='event_created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True, related_name='event_updated_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status_choice = (
        ('disabled', 'Disabled'),
        ('active', 'Active'),
        ('deleted', 'Deleted'),
        ('time out', 'Time Out'),
        ('completed', 'Completed'),
        ('cancel', 'Cancel'),
    )
    status = models.CharField(choices=status_choice, max_length=10)

    def __str__(self):
        """
        Return the name of the event.
        """
        return self.name

    def get_absolute_url(self):
        return reverse('event-list')
    
  

