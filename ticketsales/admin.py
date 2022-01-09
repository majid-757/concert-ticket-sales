from django.contrib import admin

from .models import *
# Register your models here.


class ConcertAdmin(admin.ModelAdmin):
    list_display = ["name", "singername", "length", "poster"]

admin.site.register(ConcertModel, ConcertAdmin)
admin.site.register(LocationModel)
admin.site.register(TimeModel)
admin.site.register(TicketModel)


