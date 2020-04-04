from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.utils import format_duration
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
      duration = visit.get_duration()
      visit_info = {"who_entered": visit.passcard.owner_name,
                    "entered_at": timezone.localtime(visit.entered_at),
                    "duration": format_duration(duration),
                    "is_strange": visit.is_visit_long()}
      non_closed_visits.append(visit_info)

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }

    return render(request, 'storage_information.html', context)
