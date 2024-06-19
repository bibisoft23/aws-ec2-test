from django.http import HttpResponse
from decouple import config

def index(request):
    string=config('VAR')
    return HttpResponse(string)