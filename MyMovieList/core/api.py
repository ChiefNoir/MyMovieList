from django.http.response import HttpResponse, JsonResponse, DjangoJSONEncoder

#ping-pong for tests
def ping(request):
    return HttpResponse("pong")