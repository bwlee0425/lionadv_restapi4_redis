# myapp/views.py
from django.core.cache import cache
from django.http import JsonResponse
from .models import Event
from time import time
def event_list(request):
    # 캐시에서 이벤트 목록 가져오기
    start_time = time()
    events = cache.get('events')
    if not events:
        events = list(Event.objects.all().values('name', 'date'))
        cache.set('events', events, timeout=300)  # 5분 동안 캐시 유지
    end_time = time()
    print("전체 소요 시간 : {}s".format(end_time-start_time) )
    return JsonResponse(events, safe=False)