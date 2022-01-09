from django.urls import path

from .views import ConcertListView, LocationListView, ConcertDetailsView, TimeView, ConcertEditView

urlpatterns = [
    path('concert/list', ConcertListView),
    path('location/list', LocationListView),
    path('concert/<int:concert_id>', ConcertDetailsView),
    path('time/list', TimeView),
    path('concertEdit/<int:concert_id>', ConcertEditView),

]


