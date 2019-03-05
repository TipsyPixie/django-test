from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from . import auth


@api_view(['GET'])
@csrf_exempt
def index(request):
    return Response(status=HTTP_200_OK)
