from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from apps.classroom.models import ClassRoom
from apps.student.models import Student

from uuid import UUID


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_classroom(request: Request, access_code: UUID):

    try:
        classroom = ClassRoom.objects.only('id').get(access_code=access_code)
    except ClassRoom.DoesNotExist:
        return Response({
            'message': 'The classroom does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    student, created = Student.objects.get_or_create(
        user=request.user,
        class_room__pk=classroom.id
    )

    if not created:
        if student.is_active:
            return Response({
                'message': 'You are already a student in this classroom'
            }, status=status.HTTP_400_BAD_REQUEST)

        student.is_active = True
        student.save()

    return Response({
        'message': 'Entered the classroom correctly'
    }, status=status.HTTP_200_OK)

