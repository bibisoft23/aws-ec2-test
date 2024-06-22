from django.http import HttpResponse
# from decouple import config
import os
# from os.path import join, dirname
# from dotenv import load_dotenv

# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

VAR = os.getenv("VAR")

def index(request):

    return HttpResponse(VAR)
