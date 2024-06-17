from django.db import transaction

from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status

from ..serializers import CreateHomeworkSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([FormParser, MultiPartParser])
@transaction.atomic
def create_homework(request: Request):
    create_homework_serializer = CreateHomeworkSerializer(data=request.data.dict())

    if not create_homework_serializer.is_valid():
        return Response({
            'validation_errors': create_homework_serializer.errors
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    create_homework_serializer.save()

    return Response({
        'message': 'The homework has been posted and sent to students successfully.'
    })
