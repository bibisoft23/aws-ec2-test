from django.http import HttpResponse
from decouple import config
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

VAR = os.environ.get("VAR")

def index(request):

    return HttpResponse(VAR)


# import boto3
# from botocore.exceptions import ClientError


# def get_secret():

#     secret_name = "env/aws-test"
#     region_name = "us-east-2"

#     # Create a Secrets Manager client
#     session = boto3.session.Session()
#     client = session.client(
#         service_name='secretsmanager',
#         region_name=region_name
#     )

#     try:
#         get_secret_value_response = client.get_secret_value(
#             SecretId=secret_name
#         )
#     except ClientError as e:
#         # For a list of exceptions thrown, see
#         # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
#         raise e

#     secret = get_secret_value_response['SecretString']
#     print(secret)
#     return secret
    # Your code goes here.
