from django.http import JsonResponse
from django.utils import timezone

from datetime import datetime, time


class WorkingHourseMiddlware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = timezone.localtime().time()
        print(now)
        start = time(9, 0)
        end = time(21, 59)
        print(start, end)
        if not (start <= now <=end):
            return JsonResponse(
                {"detail": "The site is only available from 09:00 to 22:00"},
                status=403
            )
        return self.get_response(request)