from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

import uuid

from apps.classroom.models import Classroom
from apps.teacher.models import Teacher


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def switch_activation_join_classroom(request: Request, classroom_id: int):
    try:
        classroom = Classroom.objects.get(pk=classroom_id)
    except Classroom.DoesNotExist:
        return Response({
            'message': 'The classroom does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    if not Teacher.objects.filter(
        user=request.user,
        classroom=classroom,
        owner=True
    ).exist():
        return Response({
            'message': 'You must be one of owners of the classroom'
        }, status=status.HTTP_400_BAD_REQUEST)

    if classroom.available_join:
        classroom.available_join = False
        classroom.save()
    else:
        classroom.available_join = True
        classroom.access_code = uuid.uuid4()
        classroom.save()

    return Response({
        'message': f'The ability to join the classroom has been {
            'activated' if classroom.available_join else 'disabled'
        }'
    }, status=status.HTTP_200_OK)

