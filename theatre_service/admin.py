from django.contrib import admin

from .models import (
    Actor,
    Genre,
    Performance,
    Play,
    Reservation,
    Ticket,
    TheatreHall,
)


admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Performance)
admin.site.register(Play)
admin.site.register(Reservation)
admin.site.register(Ticket)
admin.site.register(TheatreHall)
