from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import SearchForm, ConcertForm
from .models import ConcertModel, LocationModel, TimeModel

import ticketsales
import accounts


def ConcertListView(request):

    searchForm = SearchForm(request.GET)

    if searchForm.is_valid():
 
        SearchText = searchForm.cleaned_data["SearchText"]

        Concerts = ConcertModel.objects.filter(name__contains=SearchText)

    else:
        Concerts = ConcertModel.objects.all()

    context = {
        'concertlist': Concerts,
        'concertcount': Concerts.count(),
        'searchForm': searchForm,
    }

    return render(request, 'ticketsales/concertlist.html', context)



@login_required
def LocationListView(request):

    Locations = LocationModel.objects.all()

    context = {
        'locationlist': Locations
    }

    return render(request, 'ticketsales/locationlist.html', context)



def ConcertDetailsView(request, concert_id):

    concert = ConcertModel.objects.get(pk=concert_id)

    context = {
        'concertdetails': concert
    }


    return render(request, 'ticketsales/concertdetails.html', context)


@login_required
def TimeView(request):

    # if request.user.is_authenticated and request.user.is_active:

        times = TimeModel.objects.all()

        context = {
            'timelist': times
        }

        return render(request, 'ticketsales/timelist.html', context)

    # else:

    #     return HttpResponseRedirect(reverse(accounts.views.LoginView))



def ConcertEditView(request, concert_id):

    concert = ConcertModel.objects.get(pk=concert_id)

    if request.method == 'POST':

        concertForm = ConcertForm(request.POST, request.FILES, instance=concert)

        if concertForm.is_valid():
            concertForm.save()
            return HttpResponseRedirect(reverse(ticketsales.views.ConcertListView))
    else:

        concertForm = ConcertForm(instance=concert)

    context = {

        "concertForm": concertForm,
        "PosterImage": concert.poster
    }

    return render(request, 'ticketsales/concertEdit.html', context)



