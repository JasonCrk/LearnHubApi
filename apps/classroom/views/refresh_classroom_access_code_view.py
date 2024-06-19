from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.classroom.models import Classroom
from apps.teacher.models import Teacher

import uuid


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def refresh_classroom_access_code(request: Request, classroom_id: int):
    try:
        classroom = Classroom.objects.get(pk=classroom_id)
    except Classroom.DoesNotExist:
        return Response({
            'message': 'The classroom does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    if not Teacher.objects.filter(user=request.user, classroom=classroom, owner=True):
        return Response({
            'message': 'You are not a teacher who owns this classroom'
        }, status=status.HTTP_400_BAD_REQUEST)

    classroom.access_code = uuid.uuid4()
    classroom.save()

    return Response({
        'message': 'the classroom access code has been changed'
    })
