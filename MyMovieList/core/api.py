from django.http.response import HttpResponse, JsonResponse, DjangoJSONEncoder
from core.models import Genre, Movie
import json

#ping-pong for tests
def ping(request):
    return HttpResponse("pong")

def getGenres(request, start, end):
    result = []
    for item in Genre.objects.all()[start : end]:
        result.append(
            {
            'id': item,
            'name': 'item.name'
            }
        )
    return JsonResponse(json.dumps(result), safe=False)