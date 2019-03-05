from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from lightstage.exceptions import UserCredentialWrong, UserInactive
from lightstage.utils import parse_metadata


@api_view(['POST'])
@csrf_exempt
def sign_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request=request, username=username, password=password)
    if user is None:
        raise UserCredentialWrong()
    elif not user.is_active:
        raise UserInactive()

    login(request=request, user=user)

    metadata = parse_metadata(request)
    request.session.update(metadata)

    return Response(status=HTTP_200_OK)


@api_view(['GET'])
@csrf_exempt
def sign_out(request):
    logout(request)
    return Response(status=HTTP_200_OK)
