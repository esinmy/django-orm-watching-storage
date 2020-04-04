from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.utils import format_duration
from django.shortcuts import render
from django.utils import timezone


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    
    this_passcard_visits = []
    for visit in Visit.objects.filter(passcard__passcode=passcode):
        duration = visit.get_duration()
        visit_info = {"entered_at": timezone.localtime(visit.entered_at),
                      "duration": format_duration(duration),
                      "is_strange": visit.is_visit_long()}
        this_passcard_visits.append(visit_info)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)
