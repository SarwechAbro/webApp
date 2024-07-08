from django.contrib import admin
from .models import Venue, Event
from django.contrib.auth.models import Permission


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'codename')

#admin.site.register(Permission, PermissionAdmin)
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'phone')
	ordering = ('name',)
	search_fields = ('name', 'address')
#admin.site.register(Venue, VenueAdmin)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	fields = (('name', 'venue'), 'event_date', 'description', 'manager', 'approved')
	list_display = ('name', 'event_date', 'venue')
	list_filter = ('event_date', 'venue')
	ordering = ('event_date',)
